from typing import List


class Solution:
    def __init__(self):
        self.oranges = {}

    def orangesRotting(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        oranges = {}
        for x in range(h):
            for y in range(w):
                state = grid[x][y]
                if state > 0:
                    oranges[(x, y)] = state

        done = False
        time = 0
        while not done:
            done = True
            pre = oranges.copy()
            for (x, y), s in pre.items():
                if s != 2:
                    continue

                rot = any([
                    self.rot(oranges, x - 1, y),
                    self.rot(oranges, x + 1, y),
                    self.rot(oranges, x, y - 1),
                    self.rot(oranges, x, y + 1),
                ])

                if rot:
                    done = False

            if not done:
                time += 1

        for (x, y), s in oranges.items():
            if s != 2:
                return -1

        return time

    def rot(self, oranges, x, y):
        if not (x, y) in oranges:
            return False

        if oranges[(x, y)] > 1:
            return False

        oranges[(x, y)] = 2
        return True


print(Solution().orangesRotting([[1],[2],[1],[1]]))

