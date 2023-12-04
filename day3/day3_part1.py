import re

re_digits = r"\b(\d+)\b"
re_symbols = r"[$*+-/#]"
total_digits = []
total_symbols = []
x_coord = 0
y_coord = 0
symbols_coords = []
number_of_line = 0
with open("day3/day3_input1.txt", "r") as file:
    for line in file:
        line = line.replace(".", " ")
        digits = re.findall(re_digits, line)
        symbols = re.findall(re_symbols, line)
        total_digits.extend(digits)
        total_symbols.extend(symbols)
with open("day3/day3_input1.txt", "r") as file:
    for symbol, line in zip(total_symbols, file):
        line = line.replace(".", " ")
        print(f"Buscando '{symbol}' en la línea: '{line}'")
        x_coord = line.find(symbol)
        print(x_coord)
        symbols_coords.append((symbol, x_coord, y_coord))
        y_coord += 1

#print(symbols_coords)