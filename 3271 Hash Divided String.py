from functools import reduce


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        substrings = self.makeSubstrings(s, k)
        print(substrings)
        hash_values = [self.sumOfHashValues(substring) for substring in substrings]
        print(hash_values)
        print(self.makeString(hash_values))
        return self.makeString(hash_values)

    def makeSubstrings(self, s: str, k: int) -> list[str]:
        substrings = []
        for i in range(0, len(s), k):
            substrings.append(s[i:i + k])
        return substrings

    def sumOfHashValues(self, s: str) -> int:
        return reduce(lambda x, y: x + ord(y) - 19, s, 0) % 26

    def makeString(self, substrings: list[int]) -> str:
        print([chr(number) for number in substrings])
        return ''.join([chr(number + 97) for number in substrings])


print(Solution().stringHash('mxz', 3))
print(ord('a'))