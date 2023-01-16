# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется 
# разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

txt = input('Enter the text separated by a space:\n')
print(f'original text: {txt}')
find_txt = "abc"
lst = [i for i in txt.split() if find_txt not in i]
print(f'new text: {" ".join(lst)}')