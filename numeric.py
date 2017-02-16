# Karatsuba multiplication of two integers in strings
def karatsuba(num1, num2):
    # Converting from string to array of digits
    if isinstance(num1,str):
        return karatsuba(*[[int(c) for c in s] for s in [num1, num2]])

    # Padds array of integers of zero to make them of equal length
    def padup(num1,num2):
        if len(num1)<len(num2):
            num1,num2 = num2,num1
        num2 = [0]*(len(num1)-len(num2)) + num2
        return num1,num2

    # Sums numbers encoded as arrays of integers
    def ssum(num1, num2):
        ret = []
        carry = 0
        num1, num2 = padup(num1,num2)

        for pair in reversed(list(zip(num1,num2))):
            carry, val = divmod(carry+pair[0]+pair[1],10)
            ret.insert(0,val)
        if carry != 0:
            ret.insert(0,carry)
        return ret

    # Base case of the recursive implementation
    if len(num1)==1 and len(num2)==1:
        return num1[0] * num2[0]

    num1, num2 = padup(num1,num2)

    n = len(num1)
    half = int(n/2)
    a, b, c, d = num1[:half], num1[half:], num2[:half], num2[half:]
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    abcd = karatsuba(ssum(a,b),ssum(c,d))
    return 10**n * ac + 10**(n-half) * (abcd-ac-bd) + bd