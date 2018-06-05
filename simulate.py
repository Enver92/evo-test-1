#!/usr/bin/python3

import argparse
import random

servers = []
def fill_randomly():


def fill_mirror():
    print("Mirror")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="specify number of servers", nargs="?",
                        required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--mirror", action="store_true")
    group.add_argument("--random", action="store_true")
    args = parser.parse_args()

    if int(args.n) % 2 != 0:
        print("There should be an even number of servers!")
        return

    if args.mirror:
        print(args.n)
        fill_mirror()
    elif args.random:
        print(args.n)
        fill_randomly()


if __name__ == '__main__':
    main()
