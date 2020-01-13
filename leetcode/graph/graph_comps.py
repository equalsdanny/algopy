from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        n2n = {}
        for src, dst in edges:
            if src not in n2n:
                n2n[src] = set()
            if dst not in n2n:
                n2n[dst] = set()

            n2n[src].add(dst)
            n2n[dst].add(src)

        unvisited = set(n2n.keys())
        comps = 0

        while len(unvisited) > 0:
            comps += 1
            root = unvisited.pop()
            self.visit(root, unvisited, n2n)

        singles = n - len(n2n)
        return comps + singles

    def visit(self, root, unvisited, n2n):
        neighbors = n2n[root]
        todo = neighbors & unvisited
        while len(todo) > 0:
            tnode = todo.pop()
            unvisited.remove(tnode)
            self.visit(tnode, unvisited, n2n)
            todo &= unvisited


print(Solution().countComponents(4, [[2,3],[1,2],[1,3]]))
