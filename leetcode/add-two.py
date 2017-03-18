# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def append(self, first, last, ss):
        if first is None:
            ret = ListNode(ss)
            return (ret, ret)
        else:
            last.next = ListNode(ss)
            return (first, last.next)

    def addTwoNumbers(self, a, b):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = 0
        first = None
        last = None
        while a is not None or b is not None:
            aa = a.val if a is not None else 0
            bb = b.val if b is not None else 0
            ss = aa + bb + cur
            if ss > 9:
                ss %= 10
                cur = 1
            else:
                cur = 0

            first, last = self.append(first, last, ss)

            if a is not None:
                a = a.next
            if b is not None:
                b = b.next

        if cur != 0:
            first, last = self.append(first, last, cur)

        return first