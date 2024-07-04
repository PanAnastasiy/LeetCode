'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list_1 = ListNode(2, ListNode(4, ListNode(3)))
list_2 = ListNode(5, ListNode(6, ListNode(4)))


class Solution(object):

    @staticmethod
    def printList(head):
        while head:
            print(head.val, end="->")
            head = head.next
        print()

    @staticmethod
    def getList(head):
        numbers = []
        while head:
            numbers.append(head.val)
            head = head.next
        return numbers


    @staticmethod
    def makeList(li) -> ListNode:

        head = ListNode(li[0])
        current = head
        for index in range(1, len(li)):
            current.next = ListNode(li[index])
            current = current.next
        return head

    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        new_number = list(map(int, list(str(int(''.join(map(str, Solution.getList(l1)))[::-1]) +
                                            int(''.join(map(str, Solution.getList(l2)))[::-1])))))
        return Solution.makeList(new_number[::-1])



Solution.addTwoNumbers(list_1, list_2)



