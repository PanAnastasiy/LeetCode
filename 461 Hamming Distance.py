class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        x = bin(x)[2:][::-1]
        y = bin(y)[2:][::-1]
        if len(x) > len(y):
            y += '0' * (len(x) - len(y))
        else:
            x += '0' * (len(y) - len(x))
        print(x)
        print(y)
        for i in range(len(x)):
            if x[i] != y[i]:
               ans += 1
        return ans


print(Solution().hammingDistance(x = 3, y = 1))
