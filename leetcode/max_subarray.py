import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Divide and conquer approach.
        If n > 1: T(n) = 2T(n/2) + Θ(n)
        if n == 1: T(n) = Θ(1)

        Using master theorem, T(n) = Θ(n log(n))
        """

        def msa_rec(nums):

            if len(nums) == 1:
                return slice(0, 1), nums[0]

            mid = math.floor(len(nums) / 2)
            left = nums[:mid]
            right = nums[mid:]

            left_l, left_s = msa_rec(left)
            right_l, right_s = msa_rec(right)
            right_l = slice(right_l.start + mid, right_l.stop + mid)

            l_ms = None
            l_mr = None
            cs = 0
            for i in range(mid - 1, left_l.stop - 1, -1):
                cs += nums[i]
                if i == left_l.stop:
                    cs += left_s
                    i = left_l.start

                if l_ms is None or cs >= l_ms:
                    l_ms = cs
                    l_mr = slice(i, mid)

            if l_mr is None:
                l_mr = left_l
                l_ms = left_s

            r_ms = None
            r_mr = None
            cs = 0
            for i in range(mid, right_l.start):
                cs += nums[i]
                if i == right_l.start - 1:
                    cs += right_s
                    i = right_l.stop - 1

                if r_ms is None or cs >= r_ms:
                    r_ms = cs
                    r_mr = slice(mid, i + 1)

            if r_mr is None:
                r_mr = right_l
                r_ms = right_s

            cross_l = slice(l_mr.start, r_mr.stop)
            cross_s = r_ms + l_ms

            if cross_s >= left_s and cross_s >= right_s:
                assert sum(nums[cross_l]) == cross_s
                return cross_l, cross_s

            elif left_s > right_s:
                assert sum(nums[left_l]) == left_s
                return left_l, left_s

            else:
                assert sum(nums[right_l]) == right_s
                return right_l, right_s

        return msa_rec(nums)[1]

    def maxSubArray_bruteforce(self, nums: List[int]) -> int:
        """
        Time = O(n**2)
        """
        ms = None
        for s in range(0, len(nums)):
            cs = 0
            for e in range(s, len(nums)):
                cs += nums[e]
                if ms is None or cs > ms:
                    ms = cs

        return ms


cases = {
    (-2, 1)                              : 1,
    (2, -1, 3, 0)                        : 4,
    (-2, 1, -3, 4, -1, 2, 1, -5, 4)      : 6,
    (1, 2, -1, -2, 2, 1, -2, 1)          : 3,
    (1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4): 6
}

for input, expected_output in cases.items():
    actual_output = Solution().maxSubArray(input)
    print(f'{input} => {expected_output}')
    assert expected_output == actual_output
