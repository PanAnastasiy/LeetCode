class Solution:
    def reportSpam(self, message: list[str], bannedWords: list[str]) -> bool:
        counter = 0
        bannedWords = set(bannedWords)
        for word in message:
            if word in bannedWords:
                counter += 1
                if counter > 1:
                    return True
        return False