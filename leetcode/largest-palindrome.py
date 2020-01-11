import math


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        max_sub = None

        for start in range(0, len(s)):
            if max_sub is not None and len(s) - start < len(max_sub):
                break

            for end in range(len(s)-1, start-1, -1):
                sub = s[start:end + 1]
                half = len(sub) / 2
                if len(sub) % 2 == 0:
                    pal = sub[:int(half)] == sub[int(half):][::-1]
                else:
                    pal = sub[:math.floor(half)] == sub[math.ceil(half):][::-1]

                if pal and (max_sub is None or len(sub) > len(max_sub)):
                    max_sub = sub
                    break

        return max_sub



print(Solution().longestPalindrome("abba"))