
class Solution(object):
    def maxFrequencyElements(self, nums: list[int]) -> int:
        data = {}
        for num in nums:
            data[num] = data.get(num, 0) + 1
        freq = list(data.values())
        print(freq)
        return max(freq) * freq.count(max(freq))


sol = Solution()
print(sol.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
