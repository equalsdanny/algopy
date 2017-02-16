import core

# 1.2. Left-first, binary search of v in presorted s
def bsearch(s,v):
    if len(s) == 1:
        return 0 if s[0]==v else -1
    else:
        hls = round(len(s)/2)
        left = s[:hls]
        right = s[hls:]
        if v<=left[-1]:
            return bsearch(left,v)
        elif v>right[-1]:
            return -1
        else:
            res = bsearch(right,v)
            return -1 if res == -1 else res+hls

# 1.1 Floored square root of n
def sqrt(n):
    if n == 1:
        return 1
    return bsearch(LazyArray(round(n/2)+1, lambda x: (x+1)**2>n),True)
    
# 1.3. Index of first element in presorted s larger than v
def flarger(s,v):
    return bsearch(LazyArray(len(s),lambda x: s[x]>v),True)

# 1.4. Index of first element in presorted s such that s[i]=i
# Ordered and unique array implies that the function of index is strictly increasing,
# and f(x+1)-f(x)>=1. We want to find where f(x) intersects with g(x)=x for the first time.
# This is possible, only if f(0)<=0, because f(x) never grows slower than g(x).
# If f(0)<=0 indeed, we can simply do a binary search for the first occurance of f(x)>=x.
def fidentity(s):
    if s[0] > 0:
        return -1
    else:
        return bsearch(LazyArray(len(s),lambda x: s[x]>=x),True)
        
# 1.7. Results will contain as many duplicates as in each array
def intersect(a,b):
    if b[0]>a[-1] or b[-1]<a[0]:
        return []
    elif a[0]<b[-1]:
        a, b = b, a
    
    ret = []
    ai = 0
    bi = 0
    # Looking for values from b in a
    while bi < len(b):
        # I don't search the whole a every time for performance reasons,
        # but this obviously requires to remember what happened during last iteration
        offset = bsearch(LazyArray(len(a)-ai,lambda x: a[ai+x]>=b[bi]),True)
        # If values in b are now larger than anything that is left in a
        if offset == -1:
            return ret
            
        ai += offset        
        # Collect matches
        if b[bi] == a[ai]:
            while bi < len(b) and ai < len(a) and b[bi] == a[ai]:
                ret.append(b[bi])
                bi += 1
                ai += 1
        else:
            bi += 1
    return ret