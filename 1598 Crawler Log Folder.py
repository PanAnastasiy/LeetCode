from typing import List


class Solution:

    @staticmethod
    def minOperations(logs: List[str]) -> int:
        step = 0
        for log in logs:
            if log[0].isalnum():
                step += 1
            elif log[:2] == '..' and step != 0:
                step -= 1
        return step


print(Solution.minOperations(["d1/", "d2/", "../", "d21/", "./"]))

# ["d1/", "d2/", "./", "d3/", "../", "d31/"]
# ["d1/","d2/","../","d21/","./"]
