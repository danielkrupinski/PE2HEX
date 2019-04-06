import sys

file = bytearray(open(sys.argv[1], 'rb').read())

output = open(sys.argv[2], 'w')
output.write('static const uint8_t binary[]{\n')

byteCount = 0

for byte in file:
    output.write(hex(byte) + ', ')
    byteCount += 1
    if byteCount == 16:
        output.write('\n')
        byteCount = 0

output.write('};')
