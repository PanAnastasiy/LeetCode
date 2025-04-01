class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        answer = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                answer += 1
        return answer


print(Solution().busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4))
print(Solution().busyStudent(startTime=[4], endTime=[4], queryTime=4))
