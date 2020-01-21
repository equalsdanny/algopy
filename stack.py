class Node:
    def __init__(self, prev, value):
        self.prev = prev
        self.value = value


class Stack:
    def __init__(self):
        self._last = None
        self._size = 0

    def push(self, value):
        if self._last is None:
            prev = None
        else:
            prev = self._last

        new = Node(prev, value)
        self._last = new
        self._size += 1

    def pop(self):
        if self._last == None:
            raise Exception('Empty stack')

        value = self._last.value
        self._last = self._last.prev
        self._size -= 1

        return value

    def size(self):
        return self._size

    def reverse(self):

        v = None
        new = Stack()
        for _ in range(self.size()):
            v = self.pop()
            new.push(v)

        self._last = new._last
        self._size = new._size

    def reverse_inplace(self):
        n = self._last
        p = None

        while n is not None:
            c = n
            n = n.prev
            c.prev = p
            p = c

        self._last = p


stack = Stack()
if stack.size() != 0:
    raise Exception()

stack.push(1)

if stack.size() != 1:
    raise Exception()

stack.push(None)

if stack.size() != 2:
    raise Exception()

if stack.pop() != None:
    raise Exception()

if stack.size() != 1:
    raise Exception()

if stack.pop() != 1:
    raise Exception()

if stack.size() != 0:
    raise Exception()

a = [1, 5.0, 4, 'asd', False]
for i in a:
    stack.push(i)

stack.reverse_inplace()

b = []
for _ in range(stack.size()):
    b.append(stack.pop())


print(b)
print('Done')