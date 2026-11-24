import argparse
from src.lab_5.json_csv import json_to_csv, csv_to_json
from src.lab_5.csv_xlsx import csv_to_xlsx


def main():

    ''' Конвертирует CLI

    Args:
        json2csv: Переводит JSON в CSV
            --in: Путь к входному JSON 
            --out: Путь к выходному CSV

        csv2json: Переводит CSV в JSON
            --in: Путь к входному CSV
            --out: Путь к выходному JSON

        csv2xlsx: Переводит JSON в CSV
            --in: Путь к входному CSV
            --out: Путь к выходному XLSX
    '''

    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", description="из json в csv", help="из json в csv")
    p1.add_argument("--in", dest="input", required=True, help="Входной файл json")
    p1.add_argument(
        "--out", dest="output", required=True, help="Файл с результатом csv"
    )

    p2 = sub.add_parser("csv2json", description="из csv в json", help="из csv в json")
    p2.add_argument("--in", dest="input", required=True, help="Входной файл csv")
    p2.add_argument(
        "--out", dest="output", required=True, help="Файл с результатом json"
    )

    p3 = sub.add_parser("csv2xlsx", description="из csv в xlsx", help="из csv в xlsx")
    p3.add_argument("--in", dest="input", required=True, help="Входной файл csv")
    p3.add_argument(
        "--out", dest="output", required=True, help="Файл с результатом xlsx"
    )

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)


if __name__ == "__main__":
    main()
