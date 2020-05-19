# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = []
        second = []
        r = None
        while l1:
            first.append(str(l1.val))
            l1 = l1.next
        while l2:
            second.append(str(l2.val))
            l2 = l2.next
        first = int(''.join(first[::-1]))
        second = int(''.join(second[::-1]))
        result = str(first + second)
        for each in str(result):
            if r is None:
                r = ListNode(each)
                continue
            r = ListNode(each, next=r)
        return r
