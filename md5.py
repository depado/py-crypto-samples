# -*- coding: utf-8 -*-

import click
import hashlib

@click.command()
@click.option("--message", prompt=True)
def main(message):
    print(hashlib.md5(message.encode("utf-8")).hexdigest())

if __name__ == '__main__':
    main()
