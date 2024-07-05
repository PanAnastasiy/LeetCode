from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


linked = ListNode(5, ListNode(3, ListNode(1, ListNode(2,
                                                      ListNode(5, ListNode(1, ListNode(2)))))))
# [1,3,2,2,3,2,2,2,7]

linked_2 = (
    ListNode(1,
             ListNode(3,
                      ListNode(2,
                                    ListNode(2,
                                                ListNode(3,
                                                            ListNode(2, ListNode(2, ListNode(2, ListNode(7))))))))))

class Solution(object):

    @staticmethod
    def nodesBetweenCriticalPoints(head) -> List:
        indexes, index = [], 2
        first, second, third = head, head.next, head.next.next
        while first and second and third:
            if first.val < second.val > third.val or first.val > second.val < third.val:
                indexes.append(index)
            index += 1
            first = first.next
            second = second.next
            third = third.next
        return [min(list(map(lambda x, y: y - x, indexes[:-1], indexes[1:]))), indexes[-1] - indexes[0]]\
            if len(indexes) > 1 else [-1, -1]


print(Solution.nodesBetweenCriticalPoints(ListNode(3, ListNode(1))))
