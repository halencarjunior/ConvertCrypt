#!/bin/python3
# Developed under GPL3.0 License
# By Humberto Júnior - 2017

import codecs
import base64
import argparse
import hashlib
from urllib import request
from bs4 import BeautifulSoup

def encodeRot13(word):
    return codecs.encode(word, 'rot_13')

def decodeRot13(word):
    return codecs.decode(word, 'rot_13')

def encodeBase64(word):
    return base64.b64encode(word.encode('utf-8'))

def decodeBase64(word):
    return base64.b64decode(word).decode('utf-8')

def decodeMD5(hash_md5):
    url = 'http://md5.gromweb.com/?md5='+hash_md5
    r = request.urlopen(url)
    bsObj = BeautifulSoup(r, "html.parser")
    return bsObj.find("em",{"class":"long-content string"}).get_text()

def encodeMD5(word):
    return hashlib.md5(word.encode('utf-8')).hexdigest()

def main():
    parser = argparse.ArgumentParser(prog='ConvertCrypt', formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''

 ██████╗██████╗███╗   ████╗   ███████████████╗████████╗████████████╗██╗   ████████╗████████╗
██╔════██╔═══██████╗  ████║   ████╔════██╔══██╚══██╔══██╔════██╔══██╚██╗ ██╔██╔══██╚══██╔══╝
██║    ██║   ████╔██╗ ████║   ███████╗ ██████╔╝  ██║  ██║    ██████╔╝╚████╔╝██████╔╝  ██║
██║    ██║   ████║╚██╗██╚██╗ ██╔██╔══╝ ██╔══██╗  ██║  ██║    ██╔══██╗ ╚██╔╝ ██╔═══╝   ██║
╚██████╚██████╔██║ ╚████║╚████╔╝█████████║  ██║  ██║  ╚████████║  ██║  ██║  ██║       ██║
 ╚═════╝╚═════╝╚═╝  ╚═══╝ ╚═══╝ ╚══════╚═╝  ╚═╝  ╚═╝   ╚═════╚═╝  ╚═╝  ╚═╝  ╚═╝       ╚═╝
Version 0.0.1
''', epilog='''
Usage examples:

    - Base64
    python3 ConvertCrypt.py -S "String to Encrypt" --base64 -e
    python3 ConvertCrypt.py -H ZW5jcnlwdCB0ZXN0 --base64 -d

    - MD5
    python3 ConvertCrypt.py -S "String to Encrypt" --md5 -e
    python3 ConvertCrypt.py -H 098f6bcd4621d373cade4e832627b4f6 --md5 -d

    - ROT13
    python3 ConvertCrypt.py -S "String to Encrypt" --rot13 -e
    python3 ConvertCrypt.py -H "Fgevat gb Rapelcg" --rot13 -d

''')
    parser.add_argument('-H', '--hash', nargs='?', help='Hash')
    parser.add_argument('-S', '--string', nargs='?', help='For multiple words, use ""')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode Hash')
    parser.add_argument('-e', '--encode', action='store_true', help='Encode String')
    parser.add_argument('--md5', action='store_true', help='SSLv2 (CVE-2011-1473) (CVE-2016-0800)')
    parser.add_argument('--rot13', action='store_true', help='SSLv2 (CVE-2011-1473) (CVE-2016-0800)')
    parser.add_argument('--base64', action='store_true', help='Encrypt:  python3 ConvertCrypt.py -S "String to Encrypt" --base64 -e')
    parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
    args = parser.parse_args()

    hash_md5 = args.hash
    stringenc = args.string

    if (args.md5 == True and args.decode == True):
        print(parser.description)
        print("Searching for Hash MD5: " + hash_md5)
        print("[+] Result: " + decodeMD5(hash_md5))

    if (args.md5 == True and args.encode == True):
        print(parser.description)
        print("Encoding String " + stringenc + " to MD5")
        print("[+] Result: " + encodeMD5(stringenc))

    if (args.rot13 == True and args.decode == True):
        print(parser.description)
        print("Decode ROT13: " + hash_md5)
        print("[+] Result: " + decodeRot13(hash_md5))

    if (args.rot13 == True and args.encode == True):
        print(parser.description)
        print("Encoding to ROT13: " + stringenc)
        print("[+] Result: " + encodeRot13(stringenc))

    if (args.base64 == True and args.decode == True):
        print(parser.description)
        print("Decode BASE64: " + hash_md5)
        print("[+] Result: " + decodeBase64(hash_md5))

    if (args.base64 == True and args.encode == True):
        print(parser.description)
        print("Encoding to BASE64: " + stringenc)
        print("[+] Result: " + str(encodeBase64(stringenc),'utf-8'))

if __name__ == '__main__':
    main()
