text = input('enter integers in one line, including 3: ')
parts = text.split()
result = [int(x) for x in parts if x != '3']
print(result)
