from src.lib.text import *

text = open(0, encoding='utf-8').read()
text = normalize(text)
words = tokenize(text)
countfreq = count_freq(words)
top_5 = top_n(countfreq, 5)
flag = True

print()
print("Всего слов:", len(words))
print("Уникальных слов:", len(countfreq))
print("Топ-5:")
if flag:
    print()
    max_len = len(max(words + ["слово"], key=len))
    l = "слово" + ' '*(max_len - 5) + ' | ' + "частота"
    print(l)
    print('-'*len(l))
    for i in top_5:
            print(i[0], ' '*(max_len - len(i[0])), " | ", i[1], sep='')
else:
    for i in top_5:
        print(i[0], ": ", i[1], sep='')
print()