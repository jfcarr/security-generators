#!/usr/bin/env python3

import argparse
import random


def generate_pin(digits):
    """
    Generate a random series of numbers of length 'digits'.
    """
    random_digits = "".join(random.sample("0123456789", args.digits))

    return random_digits


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a PIN.")
    parser.add_argument(
        "-d", "--digits", type=int, help="Number of digits. (default is 4)", default=4
    )
    args = parser.parse_args()

    print(generate_pin(args.digits))
