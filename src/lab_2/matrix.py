def transpose(mat):
    if len(mat) == 0:
        return mat

    l = len(max(mat, key=len))
    ans = []
    for i in range(l): 
        a = []
        for j in mat:
            if len(j) < i + 1:
                return "ValueError"
            a.append(j[i])
        ans.append(a)
    return ans

def row_sums(mat):
    l = len(mat[0])
    ans = []
    for i in mat:
        if len(i) != l:
            return "ValueError"
        ans.append(sum(i))

    return ans


def col_sums(mat):
    l = len(max(mat, key=len))
    ans = []
    for i in range(l): 
        summ = 0
        for j in mat:
            if len(j) < i + 1:
                return "ValueError"
            summ += j[i]
        ans.append(summ)
    return ans

# вывод тест-кейсов
print()
print("1. transpose")
print()
print([[1, 2, 3]], "->", transpose([[1, 2, 3]]))
print([[1], [2], [3]], "->", transpose([[1], [2], [3]]))
print([[1, 2], [3, 4]], "->", transpose([[1, 2], [3, 4]]))
print([], "->", transpose([]))
print([[1, 2], [3]], "->", transpose([[1, 2], [3]]))
print()

print("2. row_sums")
print()
print([[1, 2, 3], [4, 5, 6]], "->", row_sums([[1, 2, 3], [4, 5, 6]]))
print([[-1, 1], [10, -10]], "->", row_sums([[-1, 1], [10, -10]]))
print([[0, 0], [0, 0]], "->", row_sums([[0, 0], [0, 0]]))
print([[1, 2], [3]], "->", row_sums([[1, 2], [3]]))
print()

print("3. col_sums")
print()
print([[1, 2, 3], [4, 5, 6]], "->", col_sums([[1, 2, 3], [4, 5, 6]]))
print([[-1, 1], [10, -10]], "->", col_sums([[-1, 1], [10, -10]]))
print([[0, 0], [0, 0]], "->", col_sums([[0, 0], [0, 0]]))
print([[1, 2], [3]], "->", col_sums([[1, 2], [3]]))
print()
