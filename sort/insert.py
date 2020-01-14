"""
Time is O(n**2)
Memory is O(n)
"""
def isort(a):
    for i in range(1, len(a)):
        v = a[i]
        for j in range(i-1, -1, -1):
            if a[j] > v:
                a[j+1] = a[j]
                a[j] = v

    return a


print(isort([4,3,1,2,4,6,7]))
