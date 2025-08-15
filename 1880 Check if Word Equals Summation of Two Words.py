class Solution:

    def getNumberOfStrings(self, word: str) -> int:
        number = ''
        for letter in word:
            number += str(ord(letter) - 97)
        return int(number)

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return (self.getNumberOfStrings(firstWord) +
                self.getNumberOfStrings(secondWord) == self.getNumberOfStrings(targetWord))
