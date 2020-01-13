from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w = len(grid)

        if w == 0:
            return 0

        h = len(grid[0])

        if h == 0:
            return 0

        unvisited = {
            (x, y)
            for x in range(w)
            for y in range(h)
        }

        islands = 0

        while len(unvisited) > 0:
            todo = {unvisited.pop()}
            unvisited.update(todo)

            is_land = self.work(grid, todo, unvisited)

            if not is_land:
                continue

            islands += 1
            while len(todo) > 0:
                self.work(grid, todo, unvisited)

        return islands

    def work(self, grid, todo, unvisited):
        w = len(grid)
        h = len(grid[0])

        x, y = todo.pop()
        if x < 0 or x >= w or y < 0 or y >= h:
            return None

        if (x, y) in unvisited:
            unvisited.remove((x, y))
        else:
            return None

        ncell = grid[x][y]
        if ncell == '0':
            return False

        todo.update({
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        })

        return True


print(Solution().numIslands([['1', '0'], ['0', '1']]))

