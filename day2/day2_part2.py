import re
import math

MAX_VALUES = {"blue": 14, "green": 13, "red": 12}
re_dcolor = {"blue": r"(\d+)\s+blue", "green": r"(\d+)\s+green", "red": r"(\d+)\s+red"}
re_game = r"\b(\d+)\b"
set_mins = []


def get_times(color_match):
    return int(color_match[0]) if color_match else 0


def process_line(line):
    sets = line.strip(" \n ").split(";")
    min_values = {color: 0 for color in MAX_VALUES}
    for set in sets:
        for color, color_pattern in re_dcolor.items():
            color_match = re.findall(color_pattern, set)
            color_times = get_times(color_match)
            min_values[color] = max(color_times, min_values[color])
    return math.prod(min_values.values())


with open("day2/day2_input2.txt", "r") as file:
    for line in file:
        set_mins.append(process_line(line))
print(sum(set_mins))
