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
![](../../images/lab_3/code_2.png)
> возвращает список слов

## 3. count_freq
![](../../images/lab_3/code_3.png)
> возвращает частоту слов
## 4. top_n
![](../../images/lab_3/code_4.png)
> составляет топ_n по частоте
### вывод
![](../../images/lab_3/task_1.png)

# Задание B — src/text_stats.py
![](../../images/lab_3/code_task_B.png)
