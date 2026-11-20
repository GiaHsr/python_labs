# Лабораторная работа 6 - CLI‑утилиты с argparse
## 1. CLI‑утилиты
### 1.1 Подкоманда cat
![](../../images/lab_6/cat_help.png)
```bash
python3 -m src.lab06.cli_text cat --input data/samples/people.csv
```
Выводит текст построчно ↑
```bash
python3 -m src.lab06.cli_text cat --input data/samples/people.csv -n
```
Вывод текст построчно с номерами ↑
![](../../images/lab_6/cat.png)
> Вывод подкоманды cat с --n
### 1.2 Подкоманда stats
![](../../images/lab_6/stats_help.png)
```bash
python3 -m src.lab06.cli_text stats --input data/samples/people.txt
```
Запуск с количеством слов по умолчанию ↑

```bash
python3 -m src.lab06.cli_text stats --input data/samples/people.txt --top 4
```
Запуск с заданным количеством слов ↑
![](../../images/lab_6/stats.png)
> Запуск программы с --top 4

## 2. CLI-конвертеры
### 2.1 Подкоманда json2csv
![](../../images/lab_6/json2csv_help.png)
```bash
python3 -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people_from_json.csv
```


### 2.2 Подкоманда csv2json
![](../../images/lab_6/csv2json_help.png)
```bash
python3 -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people_from_csv.json
```

### 2.3 Подкоманда csv2xlsx
![](../../images/lab_6/csv2xlsx_help.png)
```bash
python3 -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people_from_csv.xlsx
```