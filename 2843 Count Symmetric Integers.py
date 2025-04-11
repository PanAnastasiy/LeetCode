class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        counter = 0
        for num in range(low, high + 1):
            num = list(map(int, str(num)))
            length = len(num)
            if length % 2:
                continue
            elif sum(num[: length // 2]) == sum(num[length // 2:]):
                counter += 1
        return counter


#print(Solution().countSymmetricIntegers(1, 100))
print(Solution().countSymmetricIntegers(1200, 1230))
