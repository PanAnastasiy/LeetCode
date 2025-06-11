class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        arr1 = []
        arr2 = []
        arr1.append(nums[0])
        arr2.append(nums[1])
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        print(arr1, arr2)
        return arr1 + arr2


print(Solution().resultArray([2, 1, 3]))
print(Solution().resultArray([5, 4, 3, 8]))
print(Solution().resultArray([1,2,14,15]))