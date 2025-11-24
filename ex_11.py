line_1 = input('enter the first integers: ').split()
instruction = input('enter an instruction: ')

str_1 = [int(x) for x in line_1]
direction = instruction[0]
steps = int(instruction[1:])

n = len(str_1)
steps = steps % n

if direction == 'R' or direction == 'r':
    str_1[:] = str_1[n - steps:] + str_1[:n - steps]
else:
    str_1[:] = str_1[steps:] + str_1[:steps]

print(str_1[:])
