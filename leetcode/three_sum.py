from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        wanted = dict()
        triplets = set()

        for i, ni in enumerate(nums):
            if ni in wanted:
                for pair in wanted[ni]:
                    triplet = sorted(pair + (ni,))
                    triplets.add(tuple(triplet))

            for nj in nums[:i]:
                s = -(ni + nj)
                if s not in wanted:
                    wanted[s] = list()

                wanted[s].append((ni, nj))

        return triplets



    def threeSum_n3(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums = sorted(nums)

        rs = 0
        for i in range(len(nums)):
            rs += nums[i]

            if rs > 0:
                break

            for j in range(i + 1, len(nums)):
                if rs >= 0 and nums[j] > 0:
                    break

                rs += nums[j]

                for k in range(j + 1, len(nums)):
                    if rs >= 0 and nums[k] > 0:
                        break

                    rs += nums[k]
                    if rs == 0:
                        triplet = nums[i], nums[j], nums[k]
                        triplets.add(triplet)
                    rs -= nums[k]
                rs -= nums[j]
            rs -= nums[i]

        return triplets


print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([1,2,-2,-1]))