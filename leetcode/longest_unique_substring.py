def longsub(s):
    b = 0
    e = 0  # inclusive
    past = {}

    max_sub = None

    while e < len(s):
        c = s[e]

        if c in past:
            b = past[c] + 1

        cl = e - b + 1

        if max_sub is None or cl > len(max_sub):
            max_sub = s[b:e + 1]

        past[c] = e
        e += 1

    return max_sub


print(longsub('abcd'))
print(longsub('abcdab'))
print(longsub('abcdabcde'))
print(longsub('abcdabefb'))