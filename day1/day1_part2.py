import re

NUMBERS = {
    "nine": "9",
    "eight": "8",
    "seven": "7",
    "six": "6",
    "five": "5",
    "four": "4",
    "three": "3",
    "two": "2",
    "one": "1",
}


def read_lines(file_path) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def extract_digits(line) -> list[tuple]:
    digits = [(d, line.find(d)) for d in re.findall(r"\d", line)]
    for key, value in NUMBERS.items():
        start = line.find(key)
        if start != -1:
            digits.append((value, start))
    return sorted(digits, key=lambda x: x[1])


def calibration_value(digits) -> int:
    return sum(int(d[0][0] + d[-1][0]) for d in digits)


digits = (extract_digits(line) for line in read_lines("day1/day1_input2.txt"))
print(calibration_value(digits))
