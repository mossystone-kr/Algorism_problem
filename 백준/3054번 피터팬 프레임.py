from sys import stdin
word = stdin.readline().rstrip()
word_len = len(word)
lines = ['.','.','#','.','.']

for char_idx in range(word_len):
    if(char_idx + 1) % 3 != 0:
        lines[0] += '.#.'
        lines[1] += '#.#'
        lines[2] += f'.{word[char_idx]}.'
        lines[3] += '#.#'
        lines[4] += '.#.'
    else:
        lines[0] += '..*..'
        lines[1] += '.*.*.'
        lines[2] += f'*.{word[char_idx]}.*'
        lines[3] += '.*.*.'
        lines[4] += '..*..'
    if(char_idx + 1) % 3 == 1:
        lines[0] += '.'
        lines[1] += '.'
        lines[2] += '#'
        lines[3] += '.'
        lines[4] += '.'
if word_len % 3 == 2:
    lines[0] += '.'
    lines[1] += '.'
    lines[2] += '#'
    lines[3] += '.'
    lines[4] += '.'

for line in lines:
    print(line)