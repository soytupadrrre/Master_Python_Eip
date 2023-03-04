import hashlib
import crypt
from hmac import compare_digest as compare_hash


def crack_ntlm_hash(hash, wordlist):
    with open(wordlist, 'r') as f:
        for word in f:
            word = word.strip()
            if compare_hash(hash, hashlib.new('md4', word.encode('utf-16le')).hexdigest()):
                return word
    return None

def crack_unix_hash(hash, wordlist):
    with open(wordlist, 'r') as f:
        for word in f:
            word = word.strip()
            if compare_hash(hash, crypt.crypt(word, hash)):
                return word
    return None

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Crack NTLM and Unix hashes')
    parser.add_argument('type', help='Hash type (ntlm or unix)')
    parser.add_argument('file', help='Hash file')
    parser.add_argument('wordlist', help='Wordlist file')
    args = parser.parse_args()

    if args.type == 'ntlm':
        with open(args.file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    print(crack_ntlm_hash(line, args.wordlist))
    elif args.type == 'unix':
        with open(args.file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    print(crack_unix_hash(line, args.wordlist))