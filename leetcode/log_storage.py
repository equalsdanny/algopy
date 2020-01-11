from typing import List


class LogSystem:

    def __init__(self):
        self.data = {}

    def put(self, id: int, timestamp: str) -> None:
        self.data[id] = timestamp.split(':')

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        parts = 'Year:Month:Day:Hour:Minute:Second'.split(':')
        parts = dict(zip(
            parts,
            range(1, len(parts)+1)
        ))

        igra = parts[gra]
        s = s.split(':')[:igra]
        e = e.split(':')[:igra]

        out = []
        for i, t in self.data.items():
            t = t[:igra]
            if t >= s and t <= e:
                out.append(i)

        return out


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)

input = zip(
    ["LogSystem", "put", "put", "put", "retrieve", "retrieve"],
    [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"],
     ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
)

input = zip(
    ["LogSystem", "put", "put", "retrieve"],
    [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:02:23:59:59"],["2017:01:01:23:59:58", "2017:01:02:23:59:58", "Second"]]
)

obj = None
output = []

for op, args in input:
    r = None

    if op == "LogSystem":
        obj = LogSystem(*args)
    elif op == "put":
        r = obj.put(*args)
    elif op == "retrieve":
        r = obj.retrieve(*args)

    output.append(r)

print(output)
