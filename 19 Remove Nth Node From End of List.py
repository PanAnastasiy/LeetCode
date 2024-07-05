
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


linked = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

class Solution(object):


    @staticmethod
    def print(head):
        while head:
            print(head.val)
            head = head.next

    @staticmethod
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        buffer = ListNode(0, head)
        current, temp = buffer, buffer
        for _ in range(n + 1):
            current = current.next
        while current:
            temp = temp.next
            current = current.next
        temp.next = temp.next.next

        return buffer.next


Solution.print(Solution.removeNthFromEnd(ListNode(1, ListNode(2)), 1))
Solution.print(Solution.removeNthFromEnd(linked, 5))
