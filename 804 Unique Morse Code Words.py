from string import ascii_lowercase
from functools import reduce


class Solution:

    def __init__(self):
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
                 "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
                 "..-", "...-", ".--", "-..-", "-.--", "--.."]
        self.d = dict(zip(ascii_lowercase, morse))

    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        words = list(map(lambda x: self.findMorseRepresentation(x), words))
        return len(set(words))

    def findMorseRepresentation(self, word: str) -> str:
        return reduce(lambda x, y: x + self.d[y], word, '')


print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
