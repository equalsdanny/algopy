from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])

        obstacles = set()
        for x in range(h):
            for y in range(w):
                if obstacleGrid[x][y] == 1:
                    obstacles.add((x, y))

        frontier = {(None, None): 0}

        done = False
        while not done:
            done = True

            for current in frontier.copy():
                x, y = current

                if x == y == None:
                    start = (h-1, w-1)
                    frontier[start] = int(start not in obstacles)
                    done = False

                else:

                    if x > 0:
                        left = (x - 1, y)
                        if left not in obstacles:
                            done = False
                            if left in frontier:
                                frontier[left] += frontier[current]
                            else:
                                frontier[left] = frontier[current]

                    if y > 0:
                        up = (x, y - 1)
                        if up not in obstacles:
                            done = False
                            if up in frontier:
                                frontier[up] += frontier[current]
                            else:
                                frontier[up] = frontier[current]

                if current != (0, 0):
                    del frontier[current]

        end = (0, 0)
        return frontier[end] if end in frontier else 0



print(Solution().uniquePathsWithObstacles([
    [0,0,0],
    [0,1,0],
    [0,0,0]
]))

print(Solution().uniquePathsWithObstacles(
    [[1,0]]
))

print(Solution().uniquePathsWithObstacles(
    [[0]]
))

print(Solution().uniquePathsWithObstacles([
    [0,0,0,0],
    [0,1,0,0],
    [0,0,0,0],
    [0,0,1,0],
    [0,0,0,0]]
))

print(Solution().uniquePathsWithObstacles([
    [0,1,0,0,0],
    [1,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]))