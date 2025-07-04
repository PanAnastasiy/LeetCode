class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        answer = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            answer += abs(seats[i] - students[i])
        return answer


print(Solution().minMovesToSeat([3, 1, 5], [2, 7, 4]))
