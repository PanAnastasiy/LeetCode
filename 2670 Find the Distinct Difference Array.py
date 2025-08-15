class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        answer = []
        for i in range(len(nums)):
            answer.append(len(set(nums[:i + 1])) - len(set(nums[i + 1: ])))
        return answer


print(Solution().distinctDifferenceArray([1, 2, 3, 4, 5]))
