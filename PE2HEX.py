import sys

if len(sys.argv) < 2:
    print('Usage: PE2HEX input_filename [output_filename]\nExample: PE2HEX input.dll output.txt')
    exit(1)

file = bytearray(open(sys.argv[1], 'rb').read())

output = open(sys.argv[2] if len(sys.argv) >= 3 else 'output.txt', 'w')
output.write('static const uint8_t binary[]{\n')

byteCount = 0

for byte in file:
    output.write(f'{byte:#0{4}x}, ')
    byteCount += 1
    if byteCount == 16:
        output.write('\n')
        byteCount = 0

output.write('};')
