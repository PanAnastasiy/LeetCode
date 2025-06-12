class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        answer = 0
        binary_start = str(bin(start)[2:])
        binary_goal = str(bin(goal)[2:])
        len_start = len(binary_start)
        len_goal = len(binary_goal)
        if len_start > len_goal:
            binary_goal = '0' * (len_start - len_goal) + binary_goal
        else:
            binary_start = '0' * (len_goal - len_start) + binary_start
        i = 0
        while i < len(binary_goal):
            if binary_start[i] != binary_goal[i]:
                answer += 1
            i += 1
        return answer


print(Solution().minBitFlips(10, 7))
print(Solution().minBitFlips(3, 4))