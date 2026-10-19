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