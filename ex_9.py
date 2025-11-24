import re

text = input('Enter a sentence: ')
read = []
while text != '':
    read.append(re.findall(r'[a-zA-Zа-яА-ЯёЁ]+', text))
    text = input('Enter a sentence: ')

all_words = []
for word_list in read:
    all_words.extend(word_list)

all_words = [word.lower() for word in all_words]

word_count = {}
order = []
for word in all_words:
    if word not in word_count:
        word_count[word] = 0
        order.append(word)
    word_count[word] += 1

sorted_words = sorted(order, key=lambda word: (-word_count[word], order.index(word)))

for word in sorted_words:
    print(word)
