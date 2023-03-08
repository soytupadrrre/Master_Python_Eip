import argparse
import hashlib
import crypt
from hmac import compare_digest as compare_hash

def crack_ntlm(crypted_pass, wordlist):
    """Crackeo de hashes NTLM
    
    :param crypted_pass: Hash a descifrar
    :type crypted_pass: str
    :param wordlist: Lista de palabras
    :type wordlist: list
    :return: Palabra que genera el hash
    :rtype: str
    """
    func = lambda x: compare_hash(crypted_pass, hashlib.new('md4', x.encode('utf-16le')).hexdigest()) 
    result = list(filter(func, wordlist))
    if result:
        return result[0]
        
def crack_unix(crypted_pass, salt, wordlist):
    """Crackeo de hashes Unix
    
    :param crypted_pass: Hash a descifrar
    :type crypted_pass: str
    :param salt: Sal
    :type salt: str
    :param wordlist: Lista de palabras
    :type wordlist: list
    :return: Palabra que genera el hash
    :rtype: str
    """
    func = lambda x: compare_hash(crypted_pass, crypt.crypt(x, salt))
    result = list(filter(func, wordlist))
    if result:
        return result[0]

def brute_force(crypted_pass, wordlist, salt=None):
    """
    Función que realiza un ataque de fuerza bruta a un hash

    :param crypted_pass: Contraseña encriptada
    :type crypted_pass: str
    :param wordlist: Lista de palabras
    :type wordlist: list
    :param salt: Sal, por defecto None
    :type salt: str, optional
    :return: Palabra que genera el hash
    :rtype: str
    """
    if salt is None:
        return crack_ntlm(crypted_pass, wordlist)
    else:
        return crack_unix(crypted_pass, salt, wordlist)

def word_generator(lines, hashtype):
    """
    Generador de palabras

    :param lines: Lista de líneas
    :type lines: list
    :param hashtype: Tipo de hash
    :type hashtype: bool
    :yield: Tupla con el usuario, el hash y la sal
    :rtype: tuple
    """
    for line in lines:
        line = line.strip()
        if hashtype == "ntlm":
            password_hashed = line.split(":")[3]
            if password_hashed:
                user = line.split(":")[0]
                yield user, password_hashed, None
        elif hashtype == "unix":
            salt = f'${line.split("$")[1]}${line.split("$")[2]}$'
            password_hashed = salt + line.split("$")[3].split(":")[0]
            user = line.split(":")[0]
            yield user, password_hashed, salt

def load_file(file_path):
    """
    Carga las lineas de un archivo

    :param file_path: Ruta del archivo
    :type file_path: str
    :return: Lista de líneas
    :rtype: list
    """
    f = open(file_path, 'r')
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crack NTLM and Unix hashes')
    parser.add_argument('type', help='Hash type (ntlm or unix)', choices=['ntlm', 'unix'])
    parser.add_argument('file', help='Hash file')
    parser.add_argument('wordlist', help='Wordlist file')
    args = parser.parse_args()

    hashes = load_file(args.file)
    wordlist = load_file(args.wordlist)

    for user, password, salt in word_generator(hashes, args.type):
        result = brute_force(password, wordlist, salt)
        if not result:
            continue
        print(f"{user}: {result} | {password}")