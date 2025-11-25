text = input('enter integers in one line, including 3: ')
parts = text.split()
result = [int(x) for x in parts if x != '3']
print(result)

# Альтернатива
numbers = list(map(int, input('enter integers in one line, including 3: '").split()))

if 3 in new_list:
    numbers.remove(3)
                              
print(numbers)
