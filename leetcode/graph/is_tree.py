from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0 and n == 1:
            return True

        n2n = {}
        for src, dst in edges:
            if src not in n2n:
                n2n[src] = set()
            if dst not in n2n:
                n2n[dst] = set()

            n2n[src].add(dst)
            n2n[dst].add(src)

        if len(n2n) < n and n > 1:
            return False

        visited = set()
        todo = {next(iter(n2n))}

        while len(todo) > 0:
            node = todo.pop()

            if node in visited:
                return False
            visited.add(node)

            children = n2n[node]
            for c in children:
                n2n[c].remove(node)

            if not todo.isdisjoint(children):
                return False

            todo |= children

        return len(visited) == n


print(Solution().validTree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(Solution().validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))
print(Solution().validTree(1, []))