
class Solution:

    @staticmethod
    def truncateSentence(s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


print(Solution.truncateSentence("Hello how are you Contestant", 4))
