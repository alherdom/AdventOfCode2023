import re

CONFIG = {"blue": 14, "green": 13, "red": 12}
re_dcolor = {"blue": r"(\d+)\s+blue", "green": r"(\d+)\s+green", "red": r"(\d+)\s+red"}
re_idgame = r"\b(\d+)\b"
sum_idgames = 0


def get_times(color_match):
    return int(color_match[0]) if color_match else 0


def get_idgame(line):
    idgame_match = re.search(re_idgame, line)
    return int(idgame_match.group(1)) if idgame_match else None


def is_valid_set(set):
    for color, color_pattern in re_dcolor.items():
        color_match = re.findall(color_pattern, set)
        color_times = get_times(color_match)
        if color_times > CONFIG[color]:
            return False
    return True


def process_line(line):
    sets = line.strip(" \n ").split(";")
    return all(is_valid_set(set) for set in sets), get_idgame(line)


with open("day2/day2_input1.txt", "r") as file:
    for line in file:
        is_valid, idgame = process_line(line)
        if is_valid and idgame is not None:
            sum_idgames += idgame
print(sum_idgames)
