class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        answer = []
        for element in order:
            if element in friends:
                answer.append(element)
        return answer
