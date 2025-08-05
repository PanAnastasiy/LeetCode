from string import ascii_lowercase


class Solution:

    def findDistance(self, s: str, ch: str) -> int:
        return s.rfind(ch) - s.find(ch) - 1

    def checkDistances(self, s: str, distance: list[int]) -> bool:
        dct = dict(zip(ascii_lowercase, distance))
        for ch in set(s):
            if dct[ch] != self.findDistance(s, ch):
                return False
        return True


print(Solution().checkDistances("abaccb",
                                [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
