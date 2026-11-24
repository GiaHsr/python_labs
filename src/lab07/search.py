def linear_search(nums, x):

    '''Линейный поиск

    Args:
        nums: Список с набором чисел
        x: Искомое число

    Returns:
        i: Искомый индекс элемента списка (-1 если элемент отсутствует)

    Complexity:
        O(n): Линейная сложность
    '''

    i = -1
    for j in range(len(nums)):
        if nums[j] == x: 
            i = j
            break
    return i

def binary_search(sorted_nums, x):

    ''' Бинпоиск

    Args:
        sorted_nums: Список чисел ⁡⁢⁣⁣!отсортированный!⁡
        x: Искомое число

    Returns:
        i: Искомый индекс элемента списка (-1 если элемент отсутствует)

    Complexity:
        O(log n): Логарифмическая сложность
    '''

    i = -1
    l = 0
    r = len(sorted_nums) - 1
    while l <= r:
        m = (l + r)//2
        if sorted_nums[m] == x:
            i = m
            break
        elif sorted_nums[m] > x:
            r = m - 1
        else:
            l = m + 1
    return i

def two_sum_brute(nums, target):
    ans = ()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                ans = (i, j)
                break
        if len(ans) != 0:
            break

    if len(ans) != 0:
        return ans
    else:
        return None

def two_sum_fast(nums, target):
    d = {}
    ans = ()
    for i in range(len(nums)):
        x = nums[i]
        if (target - x) in d:
            ans = (min(i, d[target - x]), max(i, d[target - x]))
            break
        d[x] = i
    if len(ans) != 0:
        return ans
    return None
