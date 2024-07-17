
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


lst1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
lst2 = ListNode(100001, ListNode(100002, ListNode(100003)))


class Solution(object):

    @staticmethod
    def printer(head):
        while head:
            print(head.val, end=" ")
            head = head.next

    @staticmethod
    def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current_1, current_2, current_3 = list1, list2, list1
        while current_2.next:
            current_2 = current_2.next
        for _ in range(b + 1):
            current_1 = current_1.next
        current_2.next = current_1
        for _ in range(a - 1):
            current_3 = current_3.next
        current_3.next = list2
        return list1


Solution.printer(Solution.mergeInBetween(lst1, 3, 4, lst2))


