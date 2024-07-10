from typing import List


class Solution(object):

    @staticmethod
    def shuffle(nums: List[int], n: int) -> List[int]:
        answer = []
        for pair in zip(nums[:n], nums[n:]):
            answer.append(pair[0])
            answer.append(pair[1])
        return answer


print(Solution.shuffle([2, 5, 1, 3, 4, 7], 3))
