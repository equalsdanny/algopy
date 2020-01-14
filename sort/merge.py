import math

"""
Time is 
"""
def msort(a):
    if len(a) == 1:
        return a

    half = math.floor(len(a)/2)
    left = msort(a[:half])
    right = msort(a[half:])

    out = []
    i = j = 0
    while len(out) < len(a):
        if i >= len(left):
            out.append(right[j])
            j += 1

        elif j >= len(right):
            out.append(left[i])
            i += 1

        elif left[i] < right[j]:
            out.append(left[i])
            i += 1

        else:
            out.append(right[j])
            j += 1

    return out



print(msort([4,5,4,3,1,5,3]))