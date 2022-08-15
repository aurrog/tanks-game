from settings import *

text_map = ['0000000000000',
            '0101011101010',
            '0100011100010',
            '0110001000110',
            '0111100011110',
            '0000000000000',
            '1101101011011',
            '0000000000000',
            '0110111110110',
            '0010001000100',
            '0010000000100',
            '0000011100000',
            '1000010100001']

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '1':
            world_map.add((i * TILE, j * TILE))
