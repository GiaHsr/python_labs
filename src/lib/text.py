
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    ''' Нормализует текст

        casefold:
            True: Переводит все буквы в строчные

        yo2e: 
            Заменяет ё/Ё на е/Е

        Returns:
            Итоговый обработанный текст
    '''

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = text.split()
    return " ".join(text)


def tokenize(text: str) -> list[str]:

    ''' Разбивает на слова
    
        Returns:
            Массив слов
    '''

    return [match.group() for match in re.finditer(r'\w+(-\w+)*', text)]

def count_freq(tokens: list[str]) -> dict[str, int]:

    ''' Считает количество повторений токенов
    
        Returns:
            Словарь [слово], [количество повторений]
    '''

    ans = {}
    for i in tokens:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1

    return ans

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    ''' Выводит top n слов по частоте обращения
        
        Returns:
            Словарь где указаны слова и количество их повторений
    '''

    ans = list(freq.items())
 
    ans = sorted(ans, key=lambda x: (-x[1], x[0]))

    return ans[:n]