num = int(input('enter an integer: '))
div = 1
result = []
while div <= num:
    if num % div == 0:
        result.append(div)
    div += 1
print(result)
