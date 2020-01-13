import math


cache = {}

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 1:
            if target < 1 or target > f:
                return 0

            return 1

        if (d, f, target) in cache:
            return cache[(d, f, target)]

        max_x = min(target - (d - 1), f)
        min_x = target - f * (d - 1)

        rolls = 0
        for x in range(min_x, max_x+1):
            rolls += self.numRollsToTarget(d - 1, f, target - x)

        rolls = rolls % (10^9 + 7)
        cache[(d, f, target)] = rolls

        return rolls


print(Solution().numRollsToTarget(1, 6, 3))
print(Solution().numRollsToTarget(2, 6, 7))
print(Solution().numRollsToTarget(2, 5, 10))
print(Solution().numRollsToTarget(1, 2, 3))
print(Solution().numRollsToTarget(30, 30, 500))

