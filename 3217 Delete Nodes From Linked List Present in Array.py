
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        while head.val in nums:
            head = head.next
        current = head
        while current.next is not None:
            if current.next.val in nums:
                current.next = current.next.next
            current = current.next
        return head
