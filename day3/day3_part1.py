import re

re_digits = r"\b(\d+)\b"
re_symbols = r"[$*+-/#]"
digits = []
symbols = []
digits_coords = []
symbols_coords = []
num_line = 1

with open("day3/day3_input1.txt", "r") as file:
    for line in file:
        line = line.replace(".", " ")
        digits.extend(re.findall(re_digits, line))
        symbols.extend(re.findall(re_symbols, line))
        # X and Y coords of digits and symbols
        if digits:
            digits_coords.append((line.find(digits[-1]), num_line))
        else:
            digits_coords.append((None, num_line))
        if symbols:
            symbols_coords.append((line.find(symbols[-1]), num_line))
        else:
            symbols_coords.append((None, num_line))
        num_line += 1

print(digits)
print(digits_coords)
print(symbols)
print(symbols_coords)
