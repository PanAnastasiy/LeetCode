
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            result = []
            for i in range(len(s) - 1):
                result.append(str((int(s[i]) + int(s[i + 1])) % 10))
            s = ''.join(result)
        return len(set(s)) != len(s)


print(Solution().hasSameDigits("3902"))
print(Solution().hasSameDigits("34789"))
