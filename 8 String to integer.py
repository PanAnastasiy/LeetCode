
class Solution(object):
    @staticmethod
    def myAtoi(s):
        return ''.join([letter if letter.isdigit() or letter in '+-' else '|' for letter in s]).split('|')


print(Solution.myAtoi('4193 with words -78'))
