

class Solution:

    @staticmethod
    def intToRoman(num:int):
        translater = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,  'M': 1000}
        roman = ''
        while num:
            values = translater.values()
        return roman





print(Solution.intToRoman(58))
