from heap import Heap

class Task:
    def __init__(self, job, priority):
        self._job = job
        self._priority = priority

    def __lt__(self, other):
        return self._priority < other._priority

    def __eq__(self, other):
        return self._priority == other._priority

    def __str__(self):
        return 'Task[{} with {}]'.format(self._job, self._priority)

class PriorityQueue:
    def __init__(self):
        self._heap = Heap([])

    def add(self, job, priority=0):
        self._heap.add(Task(job, priority))

    def peek(self):
        return self._heap[0] if len(self._heap) > 0 else None

    def pop(self):
        return self._heap.extract()