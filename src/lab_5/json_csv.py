import csv
import json
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:

    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    source = Path(json_path)
    destination = Path(csv_path)

    # ошибки
    if source.suffix.lower() != ".json" or destination.suffix.lower() != ".csv":
        raise ValueError

    if not source.is_file():
        raise FileNotFoundError
    

    with source.open("r", encoding="utf-8") as file:
        d = json.load(file)

    if not isinstance(d, list) or not d:
        raise ValueError

    if not all(isinstance(item, dict) for item in d):
        raise ValueError
    
    keys = []
    for item in d:
        for key in item:
            if key in keys:
                continue
            else:
                keys.append(key)


    with destination.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(keys)
        for i in d:
            row = []
            for k in keys:
                row.append(i.get(k, ""))
            w.writerow(row)
    


    


def csv_to_json(csv_path: str, json_path: str) -> None:

    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    source = Path(csv_path)
    destination = Path(json_path)

    # ошибки
    if source.suffix.lower() != ".csv" or destination.suffix.lower() != ".json":
        raise ValueError
    if not source.is_file():
        raise FileNotFoundError

    with source.open("r", newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        rows = list(r)
        if not rows or not rows[0] or not any(rows[0]):
            raise ValueError

        headers = rows[0]
        row = rows[1:]
        dictt = []
        for i in row:
            if len(i) != len(headers):
                raise ValueError("не хватает данных")
            items = {}

            for j in range(len(headers)):
                items[headers[j]] = i[j]
            dictt.append(items)
        with destination.open("w", encoding="utf-8") as f:
            json.dump(dictt, f, ensure_ascii=False, indent=2)