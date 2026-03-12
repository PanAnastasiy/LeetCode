class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        answer = []
        for number in range(min(nums) + 1, max(nums)):
            if number not in nums:
                answer.append(number)

        return sorted(answer)
