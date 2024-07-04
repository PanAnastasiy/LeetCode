
class Solution:

    @staticmethod
    def isPalindrome(number):
        return str(number) == str(number)[::-1]

print(Solution.isPalindrome(121))
