import structures

char_count = structures.char_frequency('text-for-structures.txt')

for i, arr in enumerate(char_count):
    print(f"{i + 1}. line: {arr}")
