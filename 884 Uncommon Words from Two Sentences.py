class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words = s1.split() + s2.split()
        dct = {word: words.count(word) for word in set(words)}
        return list(filter(lambda x: dct[x] == 1, dct.keys()))

