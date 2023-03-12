from scapy.all import *
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', '--target', help='Target IP or IP range (192.168.1.54 or 192.168.0.0/24)', required=True)
    parser.add_argument('-i', '--interface', help='Interface to use', default="eth0")
    args = parser.parse_args()
    src_mac = get_if_hwaddr(args.interface) # MAC origen
    src_ip = get_if_addr(args.interface)# IP Origen
    ether_packet = Ether(dst=ETHER_BROADCAST)
    arp_packet = ARP(pdst=args.target, hwsrc=src_mac, psrc=src_ip)
    # ARP (Request)
    arp_request = ether_packet/arp_packet
    # ARP (Reply) => (respondidos | no respondidos)
    ans, _ = srp(arp_request, timeout=1, verbose=0)
    for _, rcv in ans:
        print(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))