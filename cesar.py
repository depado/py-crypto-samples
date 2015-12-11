# -*- coding: utf-8 -*-

import click
import sys


def caesar(plaintext, shift):
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"
    ]
    dic = {alphabet[i]: alphabet[(i+shift) % len(alphabet)] for i in range(0, len(alphabet))}
    majdict = {key.upper(): value.upper() for key, value in dic.items()}
    dic.update(majdict)
    return str.join("", [dic[found] if found in dic else found for found in plaintext])

@click.command()
@click.option('--encrypt', default=True, is_flag=True, prompt="Encrypt ? (If not, then decrypt)")
@click.option('--key', prompt="Key")
@click.option('--message', prompt="Message")
def main(key, message, encrypt):
    try:
        key = int(key)
    except:
        print("Key is not a number")
        sys.exit(1)

    if not encrypt:
        key = -key
    print()
    print(caesar(message, key))

if __name__ == '__main__':
    main()
