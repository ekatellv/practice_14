text = input('enter integers in one line: ')
parts = text.split()
num = [int(x) for x in parts]
summa = 0
for i in range(len(num)):
    summa += num[i]
print(summa / len(num))
