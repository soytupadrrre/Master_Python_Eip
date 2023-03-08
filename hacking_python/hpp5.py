import paramiko
from paramiko import SSHClient
from argparse import ArgumentParser
from colorama import Fore
from pathlib import Path
import asyncio

class SSHHost:
    """
    Clase que representa una conexión SSH a un host
    """
    
    def __init__(self, host, user, passwd):
        self.ip = host
        self.user = user
        self.passwd = passwd
        self.__set_ssh_client()

        self.stdout = None
        self.stderr = None

    def __set_ssh_client(self):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip, username=self.user,
                            password=self.passwd)
        
    def exec_command(self, command, local=None, remote=None):
        """
        Ejecuta un comando en el host remoto

        Nota: Si el comando es "put", se subirá el fichero local a la ruta remota

        :param command: Comando a ejecutar
        :type command: str
        :param local: Ruta del fichero local, defaults to None
        :type local: str, optional
        :param remote: Rutal remota donde se subirá el fichero, defaults to None
        :type remote: str, optional
        """
        if command == "put":
            self._put(local, remote)
            return f"Successfully uploaded {local} to {remote}"
        _, stdout, stderr = self.client.exec_command(command)
        self.stdout = stdout.read().decode('utf-8').strip()
        self.stderr = stderr.read().decode('utf-8').strip()

    def _put(self, local, remote):
        """
        Sube un fichero local al host remoto

        :param local: Ruta local del fichero
        :type local: str
        :param remote: Ruta remota del fichero
        :type remote: str
        :raises AssertionError: Si no se especifica local o remote
        :raises AssertionError: Si el fichero local no existe
        """
        assert local and remote
        assert Path(local).exists()
        sftp = self.client.open_sftp()
        sftp.put(local, remote)
        sftp.close()

    def close(self):
        """
        Cierra la conexión SSH
        """
        self.client.close()

# Change the hosts to your own
hosts = [
    SSHHost(host="192.168.1.44", user="pi", passwd="raspberry"),
    SSHHost(host="192.168.28.141", user="victor", passwd="victor")
]

async def execute_commands(host, command, local, remote):
    """
    Ejecuta un comando en un host remoto

    :param host: El host remoto
    :type host: SSHHost
    :param command: El comando a ejecutar
    :type command: str
    :param local: El fichero local a subir
    :type local: str
    :param remote: El fichero remoto a subir
    :type remote: str
    :return: La respuesta del host
    :rtype: str
    """
    host.exec_command(command, local, remote)
    if host.stderr:
        response = f"{Fore.LIGHTGREEN_EX}{host.user}@{host.ip}{Fore.RESET}: {Fore.BLUE}${Fore.RESET} {command}\n{host.stderr}\n"
    else:
        response = f"{Fore.LIGHTGREEN_EX}{host.user}@{host.ip}{Fore.RESET}: {Fore.BLUE}${Fore.RESET} {command}\n{host.stdout}\n"
    response += "-"*80
    #print(host.stdout)
    host.close()
    return response

async def main():
    """
    Función principal que ejecuta los comandos en los hosts remotos de forma asíncrona
    """
    tasks = [execute_commands(host, args.command, args.local, args.remote) for host in hosts]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

if __name__ == "__main__":
    parser = ArgumentParser(description="SSH Hosts")
    parser.add_argument("-c", "--command", required=True, help="Command to execute")
    parser.add_argument("-l", "--local", help="Local file to upload")
    parser.add_argument("-r", "--remote", help="Remote file to upload")
    args = parser.parse_args()

    asyncio.run(main())

    