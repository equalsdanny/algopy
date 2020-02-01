class Solution:
    def __init__(self):
        self.cache = {}

    def kSimilarity(self, A: str, B: str) -> int:
        if (A, B) in self.cache or (B, A) in self.cache:
            return self.cache[(A, B)]

        if A == B:
            return 0

        # List of K values for possible options below
        ks = []

        # What to do with A[0]?
        # Option 1: Keep as is (required if letters match)
        if A[0] == B[0]:
            ks.append(self.kSimilarity(A[1:], B[1:]))

        # Option 2: Swap letters to match B (required if letters are different)
        # Have to guess the other letter if character duplicated
        else:
            start = A.find(B[0])
            while start != -1:
                new_a = A[1:start] + A[0] + A[start + 1:]
                ks.append(1 + self.kSimilarity(new_a, B[1:]))
                start = A.find(B[0], start + 1)

        min_k = min(ks)
        self.cache[(A, B)] = min_k
        return min_k
