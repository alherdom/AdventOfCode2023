LETTERS_NUMBERS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
number = ""
numbers = []
f = open("day1.txt")
for line in f:
    for char in line:
        if char.isdigit():
            number += char
            break

    for char in line[::-1]:
        if char.isdigit():
            number += char
            break
    numbers.append(int(number))
    number = ""

result = sum(numbers)
print(result)
