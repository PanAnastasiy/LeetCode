from functools import reduce

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


linked = ListNode(1, ListNode(0, ListNode(1)))


class Solution(object):

    @staticmethod
    def getDecimalValue(head):
        number = []
        while head:
            number.append(head.val)
            head = head.next
        number = number[::-1]
        total = 0
        for weight in range(len(number)):
            if number[weight]:
                total += (2*number[weight]) ** weight
        return total


Solution.getDecimalValue(linked)
Solution.getDecimalValue(ListNode(0))
