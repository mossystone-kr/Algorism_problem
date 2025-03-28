import math

sin = math.sin
pi = math.pi

for i in range(41):
    x = i / 40.0 * 2 * pi
    character_count_per_line = int(100 * sin(x) + 100)
    output_str = '#' * character_count_per_line
    print(output_str)