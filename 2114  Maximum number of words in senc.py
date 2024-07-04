
class Solution(object):

    @staticmethod
    def mostWordsFound(sentences):
        return max(list(map(lambda x: len(x.split()), sentences)))


print(Solution.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
