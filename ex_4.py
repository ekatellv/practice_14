import re

text = input('enter a sentences: ')

words = re.findall(r'[a-zA-Zа-яА-ЯёЁ]+', text)
words_lower = [word.lower() for word in words] 

print(list(dict.fromkeys(words_lower)))
