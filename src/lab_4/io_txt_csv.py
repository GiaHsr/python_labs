from pathlib import Path
import csv
from typing import Iterable, Sequence
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    
    
    return Path(path).read_text(encoding=encoding)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
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