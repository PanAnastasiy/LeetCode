
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


lst1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
lst2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))


class Solution:
    @staticmethod
    def print(head):
        while head:
            print(head.val)
            head = head.next

    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        mid = length // 2 + (length % 2)
        while length > mid:
            head = head.next
            length -= 1
        return head


Solution.print(Solution().middleNode(lst1))
Solution.print(Solution().middleNode(lst2))
