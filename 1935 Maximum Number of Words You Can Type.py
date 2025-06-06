class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        answer = 0
        for word in text.split():
            for brokenLetter in brokenLetters:
                if brokenLetter in word:
                    break
            else:
                answer += 1
        return answer
