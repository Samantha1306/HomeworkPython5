# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encoding(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

data = print(rle_encoding(input()))
