from asyncio import tasks
from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        answer = float('inf')
        for start, end in tasks:
            if start + end < answer:
                answer = start + end
        return answer


print(Solution().earliestTime([[1,6],[2,3]]))