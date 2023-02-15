"""
Aplicación para la búsqueda de hosts vulnerables a CVE-2021-41773 en Shodan y escaneo de puertos 80 y 443 con Nmap

Script creado para la asignatura de Hacking y Pentesting con Python de la Escuela Internacional de Postgrados.

Es necesario tener instaladas las librerías de Shodan, Nmap y Pandas para el correcto funcionamiento del script.

```cmd
pip install shodan python-nmap pandas
```

**@autor:** Víctor Luque Martín </br>
**@fecha:** 02-02-2023 </br>
**@versión:** 1.0 </br>
**@email:** victorluque341@gmail.com </br>
"""
import shodan  # pip install shodan
import nmap  # pip install python-nmap
import pandas as pd  # pip install pandas
from ipaddress import ip_address, IPv4Address
from typing import List
from getpass import getpass


def get_apache_vuln_hosts_from_shodan(api: shodan.Shodan, limit: int = 5) -> List[str]:
    """
    Función que busca hosts IPv4 vulnerables a CVE-2021-41773 en Shodan

    :param api: Objeto de la API de Shodan
    :type api: shodan.Shodan
    :param limit: Límite de hosts resultantes. Por defecto 5.
    :type limit: int, optional
    :return: Lista de hosts vulnerables a CVE-2021-41773 o None si no se encuentran
    :rtype: Optional[List[str]]
    """
    hosts = set()
    cve = "CVE-2021-41773"
    page = 1

    def validate_ipv4(ip: str) -> bool:
        try:
            return type(ip_address(ip)) is IPv4Address
        except Exception:
            return False

    while len(hosts) < limit:
        try:
            resultados = api.search("apache 2.4.49", page=page)
            for result in resultados["matches"]:
                if len(hosts) >= limit:
                    break
                if "vulns" in result and \
                    cve in result["vulns"] and \
                    validate_ipv4(result["ip_str"]):
                    hosts.add(result["ip_str"])

        except shodan.APIError as e:
            print(f"Error: {e}")
            break

    return list(hosts)


def get_nmap_scan_results(hosts: List[str]) -> pd.DataFrame:
    """
    Función que escanea hosts con Nmap y obtiene un resumen de los puertos 80 y 443 (abiertos/filtrados/cerrados),
    indicando el estado, servicio y versión.

    **Example:**
    >>> get_nmap_scan_results(["host1", "host2"])
        Host  Port  Status  Service     Version
    0  host1    80  open    http        Apache httpd 2.4.49
    1  host1   443  open    ssl/http    Apache httpd 2.4.49
    2  host2    80  open    http        Apache httpd 2.4.49
    3  host2   443  open    ssl/http    Apache httpd 2.4.49

    :param hosts: Lista de hosts a escanear
    :type hosts: List[str]
    :return: Dataframe con los resultados del escaneo
    :rtype: pd.DataFrame
    """
    scanner = nmap.PortScanner()
    scan_results = pd.DataFrame(columns=["Host", "Port", "Status", "Service", "Version"])
    for host in hosts:
        # nmap host -A -p 80,443
        scanner.scan(hosts=host, ports='80,443', arguments="-A")
        for nmap_host in scanner.all_hosts():
            for port in scanner[nmap_host]["tcp"]:  # Recorremos los puertos abiertos
                scan_results.loc[len(scan_results)] = [nmap_host, port,
                                                       scanner[nmap_host]["tcp"][port]["state"],
                                                       scanner[nmap_host]["tcp"][port]["name"],
                                                       scanner[nmap_host]["tcp"][port]["version"]]
    return scan_results


if __name__ == "__main__":
    api = shodan.Shodan(getpass("Introduce tu Shodan Api: "))
    print("Buscando hosts...")
    hosts = get_apache_vuln_hosts_from_shodan(api, limit=5)
    print("Escaneando hosts...")
    results = get_nmap_scan_results(hosts) if hosts else None
    print("Mostrando resultados...")
    print(results)
