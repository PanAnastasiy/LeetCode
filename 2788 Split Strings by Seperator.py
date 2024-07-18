from typing import List


class Solution(object):

    @staticmethod
    def splitWordsBySeparator(words: List[str], separator: str) -> List[str]:
        return list(filter(lambda x: x, f'{separator}'.join(words).split(separator)))


print(Solution.splitWordsBySeparator(["one.two.three", "four.five", "six"], "."))
