from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        n2n = {}
        for c in connections:
            if c[0] not in n2n:
                n2n[c[0]] = set()

            n2n[c[0]] |= {c[1]}

            if c[1] not in n2n:
                n2n[c[1]] = set()

            n2n[c[1]] |= {c[0]}

        critical = []
        for src, dst in connections:
            n2n_ind = n2n.copy()
            n2n_ind[src] = n2n_ind[src] - {dst}
            n2n_ind[dst] = n2n_ind[dst] - {src}

            done = False
            while not done:
                n2n_new = prop(n2n_ind)
                done = n2n_new == n2n_ind
                n2n_ind = n2n_new

            for c_src, c_dsts in n2n_ind.items():
                if len(c_dsts) < n - 1:
                    critical += [[src, dst]]
                    break

        return critical

def prop(old):
    new = old.copy()
    for src, dsts in old.items():
        for dst in dsts:
            if dst in old:
                new[src] = (new[src] | old[dst]) - {src}
    return new


input = [[0,1],[1,2],[2,0],[1,3]]
print(Solution().criticalConnections(len(input), input))