
class Solution:

    def countHillValley(self, nums: list[int]) -> int:
        filtered = [nums[0]]
        for num in nums:
            if filtered[-1] != num:
                filtered.append(num)
        if len(filtered) < 3:
            return 0
        counter = 0
        for i in range(1, len(filtered) - 1):
            if filtered[i - 1] < filtered[i] > filtered[i + 1] or filtered[i - 1] > filtered[i] < filtered[i + 1]:
                counter += 1
        return counter


print(Solution().countHillValley([2, 4, 1, 1, 6, 5]))
print(Solution().countHillValley([6,6,5,5,4,1]))
print(Solution().countHillValley([6,5,10]))
