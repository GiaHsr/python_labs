import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def check_sorting(fn, trials=100):

    '''Тестирование сортировок

    Args:
        fn: Функция сортировки
        trials: Количество проверок

    Raises:
        AssertionError: '{fn.__name__} ошибся на {data}: {result}'
            Неправильная сортировка
        AssertionError: "{fn.__name__} изменила исходный список"
            Был изменен изначальный список       
    '''

    for i in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"

    print(f"OK: {trials} проверок {fn}")

def check_search(trials=100):

    '''Тестирование поиска

    Args:
        trials: Количество проверок

    Raises:
        AssertionError: 'linear_search ошиблась на ...' / 'binary_search  ошиблась на ...'
            Поиск вернул неверный индекс или не нашел существующий элемент
    '''

    for i in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        if nums and random.randint(0, 1) == 0:
            x = random.choice(nums)
        else:
            x = 101

        try:
            ind = nums.index(x)
        except ValueError:
            ind = -1

        result = linear_search(nums, x)
        assert result == ind, f"linear_search ошиблась на {nums}: {result}"


        sort_num = sorted(nums)
        result = binary_search(sort_num, x)
        if x in sort_num:
            assert 0 <= result < len(sort_num) and sort_num[result] == x, f"binary_search ошиблась на {nums}: {result}"
        else:
            assert result == -1, f"binary_search ошиблась на {nums}: {result}"
    print(f"OK: {trials} проверок linear и binary поиска")


def check_two_sum(trials = 100):

    '''Тестирование two_sum

    Args:
        trials: Количество проверок

    Raises:
        AssertionError: 'Выводятся разные результаты'
            Результаты алгоритмов разошлись
        AssertionError: 'Неправильные индексы'
            Индексы выходят за рамки/не в том порядке/равны
        AssertionError: 'Неверный ответ'
    '''

    for i in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-200, 200)

        result_brute = two_sum_brute(nums, target)
        result_fast = two_sum_fast(nums, target)

        assert (result_brute == None) == (result_fast == None), f"Выводятся разные результаты, brute={result_brute}, fast={result_fast}"

        #brute
        if result_brute != None:
            i, j = result_brute
            assert 0 <= i < j < len(nums), f"Неправильные индексы {result_brute}"
            assert nums[i] + nums[j] == target, f"Неверный ответ {result_brute}"

        #fast
            if result_fast != None:
                i, j = result_fast
                assert 0 <= i < j < len(nums), f"Неправильные индексы {result_fast}"
                assert nums[i] + nums[j] == target, f"Неверный ответ {result_fast}"
    print(f"OK: {trials} проверок two_sum")
        


 
if __name__ == "__main__":
    random.seed(42)
    print()
    for fn in (bubble_sort, selection_sort, insertion_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print()