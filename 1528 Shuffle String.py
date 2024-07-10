from typing import List


class Solution(object):

    @staticmethod
    def restoreString(s: str, indices: List[int]) -> str:
        answer = sorted(list(zip(s, indices)), key=lambda x: x[1])
        return ''.join([pair[0] for pair in answer])


print(Solution.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
