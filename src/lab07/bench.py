import csv
import timeit
import random
from src.lab_4.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
 
 
def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]
 
 
def bench_sorts(n):
    data = [random.randint(-10000, 10000) for i in range(n)]
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=100)/100
    rows.append(("sort", n, "sorted", t))

    if n >= 100_000:
        rows.append(("sort", n, "bubble_sort", "> 60c"))
        rows.append(("sort", n, "insertion_sort", "> 60c"))
        rows.append(("sort", n, "selection_sort", "> 60c"))

    else:
        t = timeit.timeit(lambda: bubble_sort(data), number=1)
        rows.append(("sort", n, "bubble_sort", t))
        
        t = timeit.timeit(lambda: insertion_sort(data), number=1)
        rows.append(("sort", n, "insertion_sort", t))
        
        t = timeit.timeit(lambda: selection_sort(data), number=1)
        rows.append(("sort", n, "selection_sort", t))
    
    return rows

def bench_search(n: int):
    data = [random.randint(-10_000, 10_000) for i in range(n)]
    queries = [random.randint(-10_0000, 10_0000) for _ in range(10_000)]
    rows = []

    t = timeit.timeit(lambda: [linear_search(data, q) for q in queries], number=1)
    rows.append(("search", n, "linear_search", t))

    sort_data = sorted(data)
    t = timeit.timeit(lambda: [binary_search(sort_data, q) for q in queries], number=1)
    rows.append(("search", n, "binary_search", t))

    return rows

def bench_two_sum(n: int):
    data = random.sample(range(-100000, 100000), n)
    rows = []
    ind1, ind2 = random.randint(0, len(data)-1), random.randint(0, len(data)-1)
    if ind1 == ind2 and ind2 + 1 < len(data):
        ind2 += 1
    elif ind1 == ind2:
        ind1 -= 1
    target = data[ind1] + data[ind2]

    t = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
    rows.append(("sum", n, "two_sum_brute", t))

    t = timeit.timeit(lambda: two_sum_fast(data, target), number=100)/100
    rows.append(("sum", n, "two_sum_fast", t))

    return rows

if __name__ == "__main__":
    random.seed(42)
    all_rows = []

    for n in [1000, 10000, 100000]:
        all_rows.extend(bench_sorts(n))

    all_rows.extend(bench_search(100000))

    for n in [1000, 10000]:
        all_rows.extend(bench_two_sum(n))

    write_csv(all_rows, "data/lab07/bench.csv", header=("task", "n", "impl", "seconds"))

