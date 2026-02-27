from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        distinct = set(c.values())
        print(distinct)
        return ((len(distinct) == 1 and distinct.pop() == 1) or
                (len(distinct) == 2 and abs(distinct.pop() - distinct.pop()) == 1))


print(Solution().equalFrequency("ddaccb"))