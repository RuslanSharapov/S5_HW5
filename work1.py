#     Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def del_letters(text):
    words = text.lower().split()
    new_words = [i for i in words if 'абв' not in i]
    new_text = ' '.join(new_words)
    return new_text

text = 'Таким Абв образом, абв всех постигнет зАБВение'
print(del_letters(text))


#  Первый тест

""" text = 'Таким Абв образом, абв всех постигнет зАБВение'
words = text.lower().split()
new_words = []
for i in words:
    if 'абв' not in i:
        new_words.append(i)

new_text = " ".join(new_words)

print(new_text) """

