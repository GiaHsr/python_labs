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

    if not d:
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

