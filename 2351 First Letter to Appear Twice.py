

class Solution(object):

    @staticmethod
    def repeatedCharacter(s: str) -> str:
        letters = []
        for letter in s:
            if letter not in letters:
                letters.append(letter)
            else:
                return letter


print(Solution.repeatedCharacter("abccbaacz"))
