from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        dct = Counter(s)
        ans = 0
        while True:
            for char in target:
                if dct[char] > 0:
                    dct[char] -= 1
                else:
                    return ans
            ans += 1
