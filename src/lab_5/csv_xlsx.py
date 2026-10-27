import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    
    """

    source = Path(csv_path)
    destination = Path(xlsx_path)

    if source.suffix.lower() != ".csv" or destination.suffix.lower() != ".xlsx":
        raise ValueError

    if not source.is_file():
        raise FileNotFoundError

    with source.open("r", newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        rows = list(r)

    if not rows or not rows[0] or not any(rows[0]):
        raise ValueError

    if len(rows) < 2:
        raise ValueError

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for i in rows:
        ws.append(i)

    for column in ws.columns:
        max_len = 0
        col_num = column[0].column_letter

        for i in column:
            if i.value:
                max_len = max(max_len, len(str(i.value)))
        ws.column_dimensions[col_num].width = max(8, max_len + 2)

    wb.save(destination)