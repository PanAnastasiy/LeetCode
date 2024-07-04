class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


linked_list = ListNode(0, ListNode(3, ListNode(1, ListNode(0,
                                                           ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))


class Solution(object):

    @staticmethod
    def print(head):
        current = head
        while current:
            print(current.val)
            current = current.next

    @staticmethod
    def mergeNodes(head) -> ListNode:
        current, new_head, total, flag,  = head.next, ListNode(), 0, True
        new_current = new_head
        while current:
            if current.val != 0:
                total += current.val
            else:
                new_current.val = total
                total = 0
                if current.next:
                    new_current.next = ListNode()
                    new_current = new_current.next
            current = current.next
        return new_head

Solution.print(Solution.mergeNodes(linked_list))
