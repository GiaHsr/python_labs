# Задание A — src/lib/text.py
## 1. normalize
```
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = text.split()
    return " ".join(text)

```
> нормализует текст

## 2. tokenize
```
def tokenize(text: str) -> list[str]:
    ans = []
    word = ""
    for i in range(len(text)):
        if text[i].isalpha() or '0' <= text[i] <= '9' or (text[i] == '-' and i > 0 and i < len(text) - 1):
            word += text[i]
        elif len(word) != 0:
            ans.append(word)
            word = ""
    if len(word) != 0:
        ans.append(word)

    return ans
```
> возвращает список слов

## 3. count_freq
```
def count_freq(tokens: list[str]) -> dict[str, int]:
    ans = {}
    for i in tokens:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1

    return ans
```
> возвращает частоту слов
## 4. top_n
```
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    ans = list(freq.items())
 
    ans = sorted(ans, key=lambda x: (-x[1], x[0]))

    return ans[:n]
```
> составляет топ_n по частоте
### вывод
![](../../images/lab_3/task_1.png)

# Задание B — src/text_stats.py

