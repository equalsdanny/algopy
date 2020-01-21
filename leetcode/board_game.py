from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        flat_board = []
        for i, row in enumerate(board[::-1]):
            flat_board += row if i % 2 == 0 else row[::-1]

        flat_board = [None] + flat_board + [None]

        path = self.findShortest(flat_board, [1])
        print(path)

        if len(path) == 0:
            return -1
        else:
            return len(path)-1

    def findShortest(self, board: List[int], prefix: list):
        loc = prefix[-1]
        options = range(loc+1, loc+6+1)
        paths = {}

        max_non_ladder = None
        for option in options:
            if board[option] is None:
                return prefix + [option-1]

            if board[option] != -1 and board[option] not in set(prefix):
                if board[board[option]+1] is None:
                    return prefix + [option]
                else:
                    paths[option] = self.findShortest(
                        board,
                        prefix + [board[option]]
                    )

            if board[option] == -1:
                max_non_ladder = option

        if max_non_ladder is not None:
            if board[max_non_ladder+1] is None:
                return prefix + [max_non_ladder]
            else:
                paths[max_non_ladder] = self.findShortest(
                    board,
                    prefix + [max_non_ladder]
                )

        if len(paths) == 0:
            return []

        paths = sorted(paths.items(), key=lambda t: len(t[1]))
        shortest = paths[0]

        return prefix + [shortest[0]] + shortest[1]


Solution().snakesAndLadders([
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]]
)

Solution().snakesAndLadders([[-1,-1,-1],[-1,9,8],[-1,8,9]])

Solution().snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]])

Solution().snakesAndLadders([[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]])

Solution().snakesAndLadders([[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]])