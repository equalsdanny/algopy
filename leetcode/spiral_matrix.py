from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]

        x = y = 0
        c = 1
        d = 'r'
        e = -1
        while True:
            out[y][x] = c

            if c == n ** 2:
                break

            c += 1

            if d == 'u':
                if y - 1 > e + 1:
                    y -= 1
                else:
                    d = 'r'
                    x += 1
                    e += 1

            elif d == 'd':
                if y + 1 < n - 1 - e:
                    y += 1
                else:
                    d = 'l'
                    x -= 1

            elif d == 'l':
                if x - 1 > e:
                    x -= 1
                else:
                    d = 'u'
                    y -= 1

            elif d == 'r':
                if x + 1 < n - 1 - e:
                    x += 1
                else:
                    d = 'd'
                    y += 1

        return out


mat = Solution().generateMatrix(4)
for row in mat:
    print(row)

