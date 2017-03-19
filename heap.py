import math

def height(n, root=0):
    return math.floor(math.log(n, 2)) - math.floor(math.log(root + 1, 2))


def parent(i):
    return math.ceil(i/2)-1


def right(heap, root=0):
    i = (root+1)*2
    if i >= len(heap):
        return None
    return i


def left(heap, root=0):
    i = (root+1)*2-1
    if i >= len(heap):
        return None
    return i


def heapify(heap, root=0):
    left_i = left(heap, root)
    right_i = right(heap, root)

    if left_i is not None and heap[left_i] > heap[root] and (right_i is None or heap[right_i] <= heap[left_i]):
        heap[root], heap[left_i] = heap[left_i], heap[root]
        heapify(heap, left_i)
    elif right_i is not None and heap[right_i] > heap[root]:
        heap[root], heap[right_i] = heap[right_i], heap[root]
        heapify(heap, right_i)


def build(array):
    for i in range(math.floor(len(array)/2),-1,-1):
        heapify(array, i)


def sort(array):
    build(array)
    size = len(array)

    for i in range(size-1,0,-1):
        array[0], array[size-1] = array[size-1], array[0]
        size -= 1
        heapify(array)

    return array


class Heap:
    def __init__(self, array):
        super()
        build(array)
        self._array = array

    def __getitem__(self, item):
        return self._array[item]

    def __setitem__(self, key, value):
        self._array[key] = value

    def __len__(self):
        return len(self._array)

    def __delitem__(self, key):
        del self._array[key]

    def add(self, item):
        self._array.append(item)
        where = len(self._array)-1
        while where != 0 and self[parent(where)] < item:
            new_where = parent(where)
            self[where], self[new_where] = self[new_where], self[where]
            where = new_where

    def extract(self, node=0):
        item = self[node]
        left_i = left(self, node)
        right_i = right(self, node)

        while left_i is not None or right_i is not None:
            if left_i is not None and (right_i is None or self[left_i] > self[right_i]):
                self[node] = self[left_i]
                node = left_i
            else:
                self[node] = self[right_i]
                node = right_i

            left_i = left(self, node)
            right_i = right(self, node)

        # Removing the hole
        del self[node]

        return item

    def print(self, level=0):
        if level > height(len(self)):
            return

        nodes = self[2**level-1:2**(level+1)-1]
        nodes.extend(['X']*(2**level - len(nodes)))
        below = max(1,2**(height(len(self))-level+1)-1)
        print(''.join([str(node)+'-'*(below) for node in nodes]))
        self.print(level+1)