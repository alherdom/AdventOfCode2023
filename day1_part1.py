import re

digits = [re.findall(r"\d", line) for line in open("day1_input1.txt")]
calibration_value = sum([int(d[0] + d[-1]) for d in digits])
print(calibration_value)
