
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

linkedList = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))


def printer(head):
    while head:
        print(head.val)
        head = head.next


class Solution(object):

    @staticmethod
    def deleteDuplicates(head):
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
                continue
            current = current.next
        return head

printer(Solution.deleteDuplicates(linkedList))