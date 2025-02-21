class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        largest = 0
        for i in range(len(gain)):
            prefix = sum(gain[:i + 1])
            if prefix > largest:
                largest = prefix
        return largest


print(Solution().largestAltitude([-5, 1, 5, 0, -7]))
print(Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
