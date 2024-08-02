
class Solution:

    @staticmethod
    def checkIfPangram(sentence: str) -> bool:
        return len(set(sentence)) == 26


print(Solution.checkIfPangram('thequickbrownfoxjumpsoverthelazydog'))
