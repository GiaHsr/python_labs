def min_max(nums):
    if len(nums) == 0:
        return "ValueError"
    ma = nums[0]
    mi = nums[0]
    for i in nums:
        if i > ma: ma = i
        if i < mi: mi = i
    return (mi, ma)

def unique_sorted(nums):
    nums = list(set(nums))
    if len(nums) <= 1:
        return nums

    m = []
    b = []
    p = nums[len(nums)//2]
    pp = []

    for i in nums:
        if i < p:
            m.append(i)
        elif i == p:
            pp.append(i)
        else:
            b.append(i)

    return unique_sorted(m) + pp + unique_sorted(b)

def flatten(mat):
    ans = []
    for i in mat:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in i:
                ans.append(j)
        else:
            return "TypeError"
    return ans
            
        
# вывод тест-кейсов
print("1. min_max")
print()
print([3, -1, 5, 5, 0], '->',  min_max([3, -1, 5, 5, 0]))
print([42], '->', min_max([42]))
print([-5, -2, -9], '->', min_max([-5, -2, -9]))
print([], "->", min_max([]))
print([1.5, 2, 2.0, -3.1], "->", min_max([1.5, 2, 2.0, -3.1]))
print()


print("2. unique_sorted")
print()
print([3, 1, 2, 1, 3], '->', unique_sorted([3, 1, 2, 1, 3]))
print([], '->', unique_sorted([]))
print([-1, -1, 0, 2, 2], '->', unique_sorted([-1, -1, 0, 2, 2]))
print([1.0, 1, 2.5, 2.5, 0], '->', unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print()


print("3. flatten")
print()
print([[1, 2], [3, 4]], '->', flatten([[1, 2], [3, 4]]))
print([[1, 2], (3, 4, 5)], '->', flatten([[1, 2], (3, 4, 5)]))
print([[1], [], [2, 3]], '->', flatten([[1], [], [2, 3]]))
print([[1, 2], "ab"], '->', flatten([[1, 2], "ab"]))