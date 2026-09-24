#!/usr/bin/env python3

import argparse
import secrets
import string


def random_string(length: int, include_special: bool = True) -> str:
    """
    Return a secure random string of the requested length.
    Includes letters, digits, and (optionally) common special characters.
    """
    alphabet = string.ascii_letters + string.digits

    if include_special:
        alphabet += "!@#$%^&*()-_=+[]{}|;:,.<>/?"

    return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description="Generate a password.")
    parser.add_argument(
        "-c",
        "--characters",
        type=int,
        help="Number of characters. (default is 12)",
        default=12,
    )
    parser.add_argument(
        "-s",
        "--special",
        action="store_true",
        help="Include special characters. (FALSE if not specified)",
        default=False,
    )
    args = parser.parse_args()

    print(random_string(args.characters, args.special))


if __name__ == "__main__":
    main()
