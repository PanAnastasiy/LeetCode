class Solution(object):
    def findWordsContaining(self, words, x):
       return list(filter(lambda a: if x in a words.index(a), words))