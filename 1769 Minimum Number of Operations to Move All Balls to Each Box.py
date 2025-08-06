
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        answer = []
        for a in range(len(boxes)):
            total = 0
            for i in range(len(boxes)):
                if boxes[i] == '1':
                    total += abs(i - a)
            answer.append(total)
        return answer


print(Solution().minOperations("001011"))
    