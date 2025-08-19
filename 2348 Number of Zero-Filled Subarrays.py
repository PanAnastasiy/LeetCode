class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        answer = 0
        counter = 0
        for num in nums:
            if num == 0:
                counter += 1
                answer += counter
            else:
                counter = 0
        return answer


print(Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0]))
