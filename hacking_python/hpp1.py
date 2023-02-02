import shodan # pip install shodan
import nmap # pip install python-nmap
import pandas as pd # pip install pandas
from typing import List

from getpass import getpass

def get_apache_vuln_hosts_from_shodan(api: shodan.Shodan, limit=5):
    hosts = set()
    cve = "CVE-2021-41773"
    page = 1
    while len(hosts) < limit:
        try:
            search = api.search("apache 2.4.49", page=page) # apache 2.4.49 => CVE-2021-41773
            for result in search["matches"]:
                if len(hosts) >= limit:
                    break
                if "vulns" in result and cve in result["vulns"]:
                    hosts.add(result["ip_str"])

        except shodan.APIError as e:
            print(f"Error: {e}")
            break

    return list(hosts) if hosts else None

def get_nmap_scan_results(hosts: List[str]):
    scanner = nmap.PortScanner()
    scan_results = []
    for host in hosts:
        scanner.scan(hosts=host, ports='80,443', arguments="-A")
        for nmap_host in scanner.all_hosts():
            for port in scanner[nmap_host]["tcp"]:
                scan_results.append([nmap_host, 
                                     port, 
                                     scanner[nmap_host]["tcp"][port]["state"], 
                                     scanner[nmap_host]["tcp"][port]["name"], 
                                     scanner[nmap_host]["tcp"][port]["version"],
                                    ])
    return pd.DataFrame(scan_results, columns=["Host", "Port", "Status", "Service", "Version"])

if __name__ == "__main__":
    api = shodan.Shodan(getpass("Introduce tu Shodan Api: "))
    print("Buscando hosts...")
    hosts = get_apache_vuln_hosts_from_shodan(api, limit=5)
    print("Escaneando hosts...")
    results = get_nmap_scan_results(hosts)
    print("Mostrando resultados...")
    print(results)
    