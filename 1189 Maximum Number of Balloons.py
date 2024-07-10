
class Solution(object):

    @staticmethod
    def maxNumberOfBalloons(text: str) -> int:
        return min([text.count(letter) // 2 if letter in 'ol' else text.count(letter) for letter in 'balon'])


print(Solution.maxNumberOfBalloons('leetcode'))
