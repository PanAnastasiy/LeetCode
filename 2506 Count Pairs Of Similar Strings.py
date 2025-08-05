class Solution:
    def similarPairs(self, words: list[str]) -> int:
        total = 0
        dct = {word: set(word) for word in words}
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if dct[words[i]] == dct[words[j]]:
                    total += 1
        return total
