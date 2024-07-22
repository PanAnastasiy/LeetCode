
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


lst_1 = ListNode(1, ListNode(2, ListNode(4)))
lst_2 = ListNode(1, ListNode(3, ListNode(4)))


class Solution(object):

    @staticmethod
    def printer(head):
        while head:
            print(head.val, end=" ")
            head = head.next

    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        new_lst = ListNode(0)
        current_3 = new_lst
        while True:
            if not l1:
                current_3.next = l2
                break
            if not l2:
                current_3.next = l1
                break
            if l1.val <= l2.val:
                current_3.next = l1
                l1 = l1.next
            else:
                current_3.next = l2
                l2 = l2.next
            current_3 = current_3.next
        return new_lst.next


Solution.printer(Solution.mergeTwoLists(lst_1, lst_2))

