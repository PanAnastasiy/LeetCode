class Solution:

    def checkIncreasing(self, arr: list[int]) -> list[int]:
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i+1]:
                return False
        return True


    def canBeIncreasing(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            buffer = nums.copy()
            buffer.pop(i)
            if self.checkIncreasing(buffer):
                return True
        return False


print(Solution().canBeIncreasing([2, 3, 1, 2]))
print(Solution().canBeIncreasing([1, 2, 10, 5, 7]))
print(Solution().canBeIncreasing([1, 1, 1, 1, 1]))
