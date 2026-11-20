import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    print()
    parser = argparse.ArgumentParser(description="CLI для анализа и вывода текста")

    sub = parser.add_subparsers(dest="cmd", required=True)

    cat_parser = sub.add_parser(
        "cat", help="Вывести содержимое файла", description="Вывести содержимое файла"
    )
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = sub.add_parser(
        "stats", help="Подсчитать частоту слов", description="Подсчитать частоту слов"
    )
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Выбираем кол-во позиций в топе"
    )

    args = parser.parse_args()

    if args.cmd == "stats" and args.top <= 0:
        parser.error("--top должен быть больше нуля")

    path = Path(args.input)

    if not path.is_file():
        raise FileNotFoundError()

    try:
        if args.cmd == "cat":
            with open(path, "r", newline="", encoding="utf-8") as f:
                data = f.readlines()

            if args.n:
                for i in range(len(data)):
                    print(f"{i+1:>4}\t{data[i]}", end="")
            else:
                for i in range(len(data)):
                    print(data[i], end="")
        elif args.cmd == "stats":
            with open(path, "r", newline="", encoding="utf-8") as f:
                data = f.read()

            normal_text = normalize(data)
            tokens = tokenize(normal_text)
            words_cnt = count_freq(tokens)
            top_words = top_n(words_cnt, int(args.top))

            print(f"Всего слов: {len(tokens)}")
            print(f"Уникальных слов: {len(words_cnt)}")
            print(f"\nТоп-{args.top} слов:")

            for word, count in top_words:
                print(f"{word}: {count}")
        print()
        print()

    except (OSError, UnicodeError) as error:
        parser.exit(1, f"Ошибка: {error}\n")


if __name__ == "__main__":
    main()
