from typing import List


class Solution(object):


    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [index for index in range(len(words)) if x in words[index]]

