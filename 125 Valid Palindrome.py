
class Solution(object):

    @staticmethod
    def isPalindrome(s):
        new_str = ''.join([letter if letter.isalpha() or letter.isdigit() else '' for letter in s]).lower()
        return new_str == new_str[::-1]

Solution.isPalindrome("A man, a plan, a canal: Panama")
