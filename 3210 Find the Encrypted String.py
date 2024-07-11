
class Solution(object):

    @staticmethod
    def getEncryptedString(s: str, k: int) -> str:
        return ''.join([s[(letter + k) % len(s)] for letter in range(len(s))])


print(Solution.getEncryptedString("dart", 3))
