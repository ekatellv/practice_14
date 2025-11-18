import re

text = input('enter a sentences: ')
words = re.findall(r'[a-zA-Zа-яА-ЯёЁ]+', text)
print(words)
