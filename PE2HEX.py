import argparse

parser = argparse.ArgumentParser(
    description='PE2HEX - PE executable to byte array converter')
parser.add_argument('input', type=str,
                    help='Input PE filename or full path')
parser.add_argument('--out', default='output.txt', type=str,
                    help='Output filename or full path')
parser.add_argument('--key', default='\0', type=str,
                    help='Encryption key ascii string')

args = parser.parse_args()
file = bytearray(open(args.input, 'rb').read())

with open(args.out, 'w') as output:
    for count, byte in enumerate(file, 1):
        output.write(
            f'{byte ^ ord(args.key[(count - 1) % len(args.key)]):#0{4}x},' + (
                '\n' if not count % 16 else ' '))
