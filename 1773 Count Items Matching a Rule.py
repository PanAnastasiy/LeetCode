from typing import List


class Solution(object):

    @staticmethod
    def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        data, total = {'type': 0, 'color': 1, 'name': 2}, 0
        for item in items:
            if item[data[ruleKey]] == ruleValue:
                total += 1
        return total


print(Solution.countMatches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
                             ["phone", "gold", "iphone"]], "color", "silver"))
