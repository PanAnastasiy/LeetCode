
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word[:word.find(ch) + 1][::-1] + word[word.find(ch) + 1:]


sol = Solution()
print(sol.reversePrefix("abcdefd", "r"))
