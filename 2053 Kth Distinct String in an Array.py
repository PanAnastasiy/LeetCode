from typing import List


class Solution:

    @staticmethod
    def kthDistinct(arr: List[str], k: int) -> str:
        answer = list(filter(lambda x: x[1] == 1, [(n, arr.count(n)) for n in arr]))
        print(answer)
        return answer[k - 1][0] if k <= len(answer) else ""


print(Solution.kthDistinct(["d","b","c","b","c","a"], 2))
