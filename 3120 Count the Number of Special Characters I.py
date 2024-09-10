class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        total = 0
        for letter in set(word):
            if letter.islower() and letter.upper() in word or letter.isupper() and letter.lower() in word:
                total += 1
        return total // 2


sol = Solution()
print(sol.numberOfSpecialChars('aaAbcBC'))
