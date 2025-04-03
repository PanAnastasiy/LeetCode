class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        dct = {num: nums.count(num) for num in set(nums)}
        counter = 0
        for pair in dct.items():
            if pair[1] % 2:
                counter += 1
        return [(len(nums) - counter) // 2, counter]


print(Solution().numberOfPairs([1, 3, 2, 1, 3, 2, 2]))
