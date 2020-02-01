from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(prefix, depth, rem):
            op = rec(prefix + '(', depth + 1, rem - 1) if rem > 0 else []
            cl = rec(prefix + ')', depth - 1, rem) if depth > 0 else []
            full = [prefix] if rem == depth == 0 else []

            return op + cl + full

        return rec('', 0, n)


print(Solution().generateParenthesis(3))