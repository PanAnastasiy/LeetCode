
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

class Solution(object):

    @staticmethod
    def print(head):
        while head:
            print(head.val)
            head = head.next

    @staticmethod
    def makeListNode(head, new_head):
        if head.next:
            Solution.makeListNode(head.next, new_head)
            new_head.next = head.next
        else:
            return n


    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        new_head = ListNode(0)
        Solution.print(Solution.makeListNode(head, new_head)
        return new_head.next


Solution.print(Solution.reverseList(linkedList))
