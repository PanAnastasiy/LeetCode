
class Solution:

    @staticmethod
    def finalString(s: str) -> str:
        new_s = ''
        for symbol in s:
            if symbol != 'i':
                new_s += symbol
            else:
                new_s = new_s[::-1]
        return new_s


print(Solution.finalString('string'))
