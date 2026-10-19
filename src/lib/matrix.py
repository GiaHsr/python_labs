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