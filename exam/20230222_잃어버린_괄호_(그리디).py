import re

regex = re.compile(r'[+|-]?\d+')
matches = list(map(int, regex.findall(input())))

is_minus = False
result = 0
for num in matches:
    if not is_minus and num < 0:
        is_minus = True

    if is_minus:
        result -= abs(num)
    else:
        result += num
print(result)
