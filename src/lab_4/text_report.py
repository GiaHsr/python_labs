import argparse
from src.lab_4.io_txt_csv import read_text, write_csv
from src.lib.text import count_freq, normalize, tokenize, top_n

parser = argparse.ArgumentParser()
parser.add_argument("--in", dest="inp", default="data/lab04/input.txt")
parser.add_argument("--out", default="data/report.csv")
parser.add_argument("--encoding", default="utf-8")
args = parser.parse_args()

''' Пример вызова:
python3 -m src.lab_4.text_report --in data/lab04/input.txt --out data/out.csv
'''

text = read_text(args.inp, encoding=args.encoding)

norm = normalize(text)
tokens = tokenize(norm)
freq = count_freq(tokens)
top = top_n(freq, n=len(freq))

write_csv(top, args.out, header=("word", "count"))
print()
print("Всего слов:", len(tokens))
print("Уникальных слов:", len(freq))
print("Топ-5:")
ans = 0
for i, j in top:
    print(i, ':', j, sep = '')
    ans += 1
    if ans == 5:
        break
print()