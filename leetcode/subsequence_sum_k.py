from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subs = []
        ps = {}

        rs = 0
        for end in range(len(nums)):
            rs += nums[end]

            if rs not in ps:
                ps[rs] = []

            ps[rs].append(end)

        rem = k
        for start in range(0, len(nums)):
            if rem in ps:
                for end in ps[rem]:
                    if end+1 > start:
                        subs.append(nums[start:end + 1])
            rem += nums[start]

        return len(subs)


print(Solution().subarraySum([-1,-1,1], 0))
print(Solution().subarraySum([1,2,3], 3))