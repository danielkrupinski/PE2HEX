import sys

if len(sys.argv) < 2:
    print('Usage: PE2HEX input_filename [output_filename]\nExample: PE2HEX input.dll output.txt')
    exit(1)

file = bytearray(open(sys.argv[1], 'rb').read())

output = open(sys.argv[2] if len(sys.argv) >= 3 else 'output.txt', 'w')
output.write('static const uint8_t binary[]{\n')

for count, byte in enumerate(file, 1):
    output.write(f'{byte:#0{4}x},' + ('\n' if not count % 16 else ' '))

output.write('};')
