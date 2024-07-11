
class Solution(object):

    @staticmethod
    def clearDigits(s: str) -> str:
        first_pointer = 0
        while first_pointer < len(s):
            if s[first_pointer].isdigit():
                s = s.replace(s[first_pointer - 1: first_pointer + 1], '')
                first_pointer -= 1
            else:
                first_pointer = first_pointer + 1
        return s


print(Solution.clearDigits("cb34"))
