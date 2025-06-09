class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        dct = {a: nums.count(a) for a in set(nums) if a % 2 == 0}
        if not len(dct):
            return 0
        return sorted(dct.items(), key=lambda x: (-x[1], x[0]), reverse=True)[-1][0]


print(Solution().mostFrequentEven([0, 1, 2, 2, 4, 4, 1]))
