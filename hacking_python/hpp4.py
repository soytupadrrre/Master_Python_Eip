from scapy.all import *
from ipaddress import IPv4Network
import asyncio
from argparse import ArgumentParser

async def arp_scan(src_mac, src_ip, dest_ip):
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
    src_mac = get_if_hwaddr('eth0')
    src_ip = get_if_addr('eth0')
    try:
        if "/" in args.target:
            network = IPv4Network(args.target)
        else:
            network = IPv4Network(f"{args.target}/32")
    except ValueError as e:
        print(e)
        print("Invalid IP range")
        return
    tasks = [arp_scan(src_mac, src_ip, str(ip)) for ip in network]
    results = await asyncio.gather(*tasks)
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