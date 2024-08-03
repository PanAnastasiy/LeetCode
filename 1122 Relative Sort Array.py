from typing import List


class Solution:

    @staticmethod
    def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
        data = dict.fromkeys(arr2)
        for key in data:
            data[key] = arr1.count(key)
        answer = []
        for key, value in data.items():
            answer.extend([key] * value)
        buffer = []
        for elem in arr1:
            if elem not in data:
                buffer.append(elem)
        answer.extend(sorted(buffer))
        return answer


print(Solution.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))