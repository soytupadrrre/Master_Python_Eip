from scapy.all import *
from ipaddress import IPv4Network
import asyncio
from argparse import ArgumentParser

async def arp_scan(src_mac: str, src_ip: str, dest_ip: str) -> bool:
    """
    Asynchronous ARP scan using scapy

    :param src_mac: Source MAC address
    :type src_mac: str
    :param src_ip: Source IP address
    :type src_ip: str
    :param dest_ip: Destination IP address
    :type dest_ip: str
    :return: True if the IP is alive, False otherwise
    :rtype: bool
    """
    ether_packet = Ether(dst=ETHER_BROADCAST)
    arp_packet = ARP(hwsrc=src_mac, hwdst=ETHER_BROADCAST, psrc=src_ip, pdst=dest_ip)
    arp_request = ether_packet/arp_packet
    print(f"Scanning {dest_ip}") if verbose else None
    arp_reply = srp(arp_request, timeout=1, verbose=0)
    if arp_reply and arp_reply[0]:
        return True
    else:
        return False

async def main(args):
    """
    Main function

    :param args: Arguments
    :type args: argparse.Namespace
    """
    src_mac = get_if_hwaddr('eth0')
    src_ip = get_if_addr('eth0')
    try:
        # Create an IPv4Network object from the target IP or IP range
        if "/" in args.target:
            network = IPv4Network(args.target)
        else:
            network = IPv4Network(f"{args.target}/32")
    except ValueError as e:
        print("Invalid IP range")
        return
    # Create a list of coroutines
    tasks = [arp_scan(src_mac, src_ip, str(ip)) for ip in network]
    # Run the coroutines concurrently
    results = await asyncio.gather(*tasks)
    # Print the results
    for ip, result in zip(network, results):
        if result:
            print(f"{ip} is alive")

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', '--interface', help='Interface to use', default="eth0")
    parser.add_argument('-t', '--target', help='Target IP or IP range (192.168.1.54 or 192.168.0.0/24)', required=True)
    parser.add_argument('-v', '--verbose', help="Enable verbosity", action='store_true')
    args = parser.parse_args()
    global verbose
    verbose = args.verbose
    asyncio.run(main(args))