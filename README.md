# security-generators

Generate complex passwords and pin numbers

## Usage

Password generator:

```bash
./password_generator.py --help
```

```
usage: password_generator.py [-h] [-c CHARACTERS] [-s]

Generate a password.

options:
  -h, --help            show this help message and exit
  -c CHARACTERS, --characters CHARACTERS
                        Number of characters. (default is 12)
  -s, --special         Include special characters. (FALSE if not specified)
```

PIN generator:

```bash
./pin_generator.py --help
```

```
usage: pin_generator.py [-h] [-d DIGITS]

Generate a PIN.

options:
  -h, --help            show this help message and exit
  -d DIGITS, --digits DIGITS
                        Number of digits. (default is 4)
```
