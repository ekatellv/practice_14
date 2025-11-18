import re

text = input('enter 10 integers in one line: ')
parts = re.split(r'[., ]+', text)
num = [int(x) for x in parts]
result = []
for i in range(8):
    number = num[i] + num[i + 1]
    result.append(number)
print(result)
