#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def compress(data):
    result = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(data[i - 1] + str(count))
            count = 1
    result.append(data[-1] + str(count))
    return ''.join(result)

data = 'aaabbbcccc'
compressed_data = compress(data)
print(compressed_data)


def decompress(data):
    result = []
    i = 0
    while i < len(data):
        count = int(data[i + 1])
        result.append(data[i] * count)
        i += 2
    return ''.join(result)

data = 'a3b3c4'
decompressed_data = decompress(data)
print(decompressed_data)
