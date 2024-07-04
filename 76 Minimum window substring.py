class Solution(object):

    @staticmethod
    def minWindow(s, t):
        letters_t = list(t)
        if not all([letter in s for letter in t]):
            return ""


print(Solution.minWindow('ADOBECODEBANC', 'ABC'))
