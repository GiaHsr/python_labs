def bubble_sort(nums):

    ''' Сортировка пузырьком

    Args:
        nums: Список чисел

    Returns:
        m: Отсортированный список чисел

    Complexity:
        O(n**2): Квадратичная сложность
    '''

    m = list(nums)
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if m[j - 1] > m[j]:
                m[j - 1], m[j] = m[j], m[j - 1]
    return m

 
def insertion_sort(nums):

    '''Сортировка вставками

    Args:
        nums: Список чисел

    Returns:
        arr: Отсортированный список чисел

    Complexity:
        O(n**2): Квадратичная сложность
    '''

    nums = list(nums)

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums

 
def selection_sort(nums):

    ''' Сортировка выбором

    Args:
        nums: Список чисел

    Returns:
        arr: Отсортированный список чисел

    Complexity:
        O(n**2): Квадратичная сложность
    '''

    m = list(nums)
    for i in range(len(nums)):
        mi = m[i]
        ind = i
        for j in range(i, len(nums)):
            if m[j] < mi:
                mi = m[j]
                ind = j
        m[ind], m[i] = m[i], m[ind]
    return m