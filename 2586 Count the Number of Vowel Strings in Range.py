class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        counter = 0
        for i in range(left, right + 1):
            if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou':
                counter += 1
        return counter
