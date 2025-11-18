text = input('enter integers in one line: ')
parts = text.split()
num = [int(x) for x in parts]
even = 0
odd = 0
for i in num:
    if i % 2 == 0:
        even += i
    else:
        odd += i
print(even, odd)
