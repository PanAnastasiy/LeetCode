
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


linked = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))


class Solution(object):

    def findGCD(self, first, second) -> int:
        while first != 0 and second != 0:
            if first > second:
                first = first % second
            else:
                second = second % first
        return first + second

    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            temp = current.next
            current.next = ListNode(self.findGCD(current.val, current.next.val), temp)
            current = current.next.next
        return head



sol = Solution()
sol.print(sol.insertGreatestCommonDivisors(linked))