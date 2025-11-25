text_1 = input('enter first integers: ').split()
text_2 = input('enter second integers: ').split()
begin_range = int(input('enter begin range: '))
end_range = int(input('enter end range: '))

lst_1 = [int(x) for x in text_1]
lst_2 = [int(x) for x in text_2]

# Основываясь на примере из условия
start_ind = begin_range - 1
end_ind = end_range + 1

elements = lst_1[start_ind:end_ind]
elements.reverse()

lst_2.extend(elements)
del lst_1[start_ind:end_ind]

print('The first list: ', lst_1)
print('The second list: ', lst_2)
