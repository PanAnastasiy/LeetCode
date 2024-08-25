class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        answer = []
        data = {**dict.fromkeys("qwertyuiop", 1), **dict.fromkeys("asdfghjkl", 2),
                **dict.fromkeys("zxcvbnm", 3)}
        for word in words:
            if len(set([data[letter] for letter in word.lower()])) == 1:
                answer.append(word)
        return answer


sol = Solution()
print(sol.findWords(["Hello", "Alaska", "Dad", "Peace"]))
