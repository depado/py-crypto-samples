# -*- coding: utf-8 -*-

import click


def xor(data, key):
    l = len(key)
    return bytearray(((data[i] ^ key[i % l]) for i in range(0, len(data))))

@click.command()
@click.option("--file", prompt=True)
@click.option("--xorkey", prompt=True)
def main(file, xorkey):
    key = bytearray(bytes(xorkey, 'utf-8'))
    data = bytearray(open(file, 'rb').read())
    with open("out.jpg", "wb") as fd:
        new_data = xor(data, key)
        has_23 = [pos for pos, x in enumerate(new_data) if x == 23]
        has_0 = [pos for pos, x in enumerate(new_data) if x == 0]
        for pos in has_23:
            new_data[pos] = 0
        for pos in has_0:
            new_data[pos] = 23

        has_78 = [pos for pos, x in enumerate(new_data) if x == 78]
        has_66 = [pos for pos, x in enumerate(new_data) if x == 66]
        for pos in has_78:
            new_data[pos] = 66
        for pos in has_66:
            new_data[pos] = 78

        has_36 = [pos for pos, x in enumerate(new_data) if x == 36]
        has_144 = [pos for pos, x in enumerate(new_data) if x == 144]
        for pos in has_36:
            new_data[pos] = 144
        for pos in has_144:
            new_data[pos] = 36

        fd.write(new_data)

if __name__ == '__main__':
    main()
