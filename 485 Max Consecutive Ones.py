class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        s = ''.join(map(str, nums))
        print(s)
        answer = 0
        for i in range(len(nums)):
            if '1' * (i + 1) in s:
                answer += 1
            else:
                return answer
        return answer


print(Solution().findMaxConsecutiveOnes([1]))
