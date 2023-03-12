from scapy.all import *
from argparse import ArgumentParser

def main(args):
    """
    Main function

    :param args: Arguments
    :type args: argparse.Namespace
    """
    ether_packet = Ether(dst=ETHER_BROADCAST)
    arp_packet = ARP(pdst=args.target)
    arp_request = ether_packet/arp_packet
    ans, _ = srp(arp_request, timeout=1, verbose=0)
    for _, rcv in ans:
        print(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', '--target', help='Target IP or IP range (192.168.1.54 or 192.168.0.0/24)', required=True)
    args = parser.parse_args()
    main(args)