from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = 0

        stock = self.stom(chars)

        for w in words:
            usage = self.stom(w)
            good = True
            for i, c in usage.items():
                if i not in stock or stock[i] < c:
                    good = False
                    break
            if good:
                s += len(w)

        return s

    def stom(self, s):
        stock = {}
        for c in s:
            if c not in stock:
                stock[c] = 0
            stock[c] += 1

        return stock


print(Solution().countCharacters(["cat","bt","hat","tree"], "atach"))
print(Solution().countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))