import paramiko
from paramiko import SSHClient
from argparse import ArgumentParser
from colorama import Fore
from pathlib import Path
import asyncio

class SSHHost:
    
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
        if command == "put":
            self._put(local, remote)
            command = f"ls {remote}"
        _, stdout, stderr = self.client.exec_command(command)
        self.stdout = stdout.read().decode('utf-8').strip()
        self.stderr = stderr.read().decode('utf-8').strip()

    def _put(self, local, remote):
        sftp = self.client.open_sftp()
        sftp.put(local, remote)
        sftp.close()

    def close(self):
        self.client.close()

# Change the hosts to your own
hosts = [
    SSHHost(host="192.168.1.44", user="pi", passwd="raspberry"),
    SSHHost(host="192.168.28.141", user="victor", passwd="victor")
]

async def execute_commands(host, command, local, remote):
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
    
    if args.command == "put":
        assert args.local and args.remote, "You must specify local and remote files"
        assert Path(args.local).exists(), "Local file does not exist"

    asyncio.run(main())

    