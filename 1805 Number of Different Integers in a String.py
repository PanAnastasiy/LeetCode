class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for char in word:
            if char.isalpha():
                word = word.replace(char, ' ')
        word = set(map(int, word.strip().split()))
        return len(word)


print(Solution().numDifferentIntegers("a123bc34d8ef34"))
