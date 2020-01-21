def solution(matrix):
    n = len(matrix)
    out = []
    for i in range(n):
        out.append([
            matrix[n - 1 - j][i]
            for j in range(n)
        ])

    return out


print(solution([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))