import re
import math

CONFIG = {"blue": 14, "green": 13, "red": 12}
re_dcolor = {"blue": r"(\d+)\s+blue", "green": r"(\d+)\s+green", "red": r"(\d+)\s+red"}
re_idgame = r"\b(\d+)\b"
total_power = 0


def get_times(color_match):
    return int(color_match[0]) if color_match else 0


def calc_power(line):
    sets = line.strip(" \n ").split(";")
    max_values = {color: 0 for color in CONFIG}
    for set in sets:
        for color, color_pattern in re_dcolor.items():
            color_match = re.findall(color_pattern, set)
            color_times = get_times(color_match)
            max_values[color] = max(color_times, max_values[color])
    return math.prod(max_values.values())


with open("day2/day2_input2.txt", "r") as file:
    for line in file:
        total_power += calc_power(line)
print(total_power)
