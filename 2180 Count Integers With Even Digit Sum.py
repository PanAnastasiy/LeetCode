class Solution:
    def countEven(self, num: int) -> int:
        counter = 0
        for number in range(2, num + 1):
            if not sum([int(digit) for digit in str(number)]) % 2:
                counter += 1
        return counter


print(Solution().countEven(4))
print(Solution().countEven(30))
