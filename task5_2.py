# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

with open('text_file.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Please, input text for encoding: '))
with open('text_file.txt', 'r') as file:
    my_txt = file.readline()
    txt_compr = my_txt.split()
print(my_txt)

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string

with open('text_file.txt', 'r') as file:
    decoded_string = file.read()



print('Encoded text: \t' + rle_encode(decoded_string))

