from typing import List


class Solution:

    @staticmethod
    def sortPeople(names: List[str], heights: List[int]) -> List[int]:
        data = sorted(list(zip(names, heights)), key=lambda x: -x[1])
        return [pair[0] for pair in data]


print(Solution.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
