from pathlib import Path
import csv
from typing import Iterable, Sequence
def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    ''' Читает файл и возвращает его содержимое одной строкой
                path: путь к файлу
                encoding: кодировка файла, по умолчанию - utf-8
                    для другой нужно передать ее явно
                    например, read_text(...., encoding = "cp1251")
            FileNotFoundError: если файл не найден
            UnicodeDecodeError: при несовпадениии кодировки
            Returns:
                файл в виде строки
    '''
    
    
    return Path(path).read_text(encoding=encoding)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:

    ''' Записывает частоты слов в CSV файл
            rows: список данных строк
            path: путь к файлу
            header: заголовок
        ValueError: если строки разной длинны
    '''


    if rows:
        width = len(rows[0])
        for i in rows:
            if len(i) != width:
                raise ValueError("Разные длины строк")
    with Path(path).open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for i in rows:
            w.writerow(i)


txt = read_text("data/lab04/input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "data/check.csv")
