from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []

        intervals = sorted(intervals, key=lambda i: i[0])

        last_start = None
        last_end = -1

        for start, end in intervals:
            if last_end < start:
                # new interval
                if last_start is not None:
                    output.append((last_start, last_end))
                last_start = start

            last_end = end

        return intervals


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))