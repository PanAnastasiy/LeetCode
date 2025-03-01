
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


linkedList = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
linkedList2 = ListNode(1, ListNode(2))

def printer(head):
    while head:
        print(head.val)
        head = head.next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        first = head
        second = head

        if not first.next:
            return True
        while second != None and second.next != None:
            stack.append(first.val)
            first = first.next
            second = second.next.next

        if second:
            first = first.next


        while first:
            print(stack[-1], first.val)
            if stack[-1] != first.val:
                return False
            stack.pop()
            first = first.next
        return True


print(Solution().isPalindrome(linkedList))
print(Solution().isPalindrome(linkedList2))
