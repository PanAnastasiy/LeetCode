class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []
        dct = {a: s.count(a) for a in set(s) if a.isdigit()}
        for elem in set(s):
            if elem.isdigit():
                digits.append(int(elem))
        if len(digits) < 2:
            return -1
        digits.sort()
        return digits[-2]


print(Solution().secondHighest("dfa12321afd"))
