class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        new_str = bin(n)[::-1][:-2]
        print(new_str)
        odd, even = 0, 0
        for i in range(len(new_str)):
            if new_str[i] == '1':
                if i % 2:
                    odd += 1
                else:
                    even += 1
        return [even, odd]


print(Solution().evenOddBit(50))
