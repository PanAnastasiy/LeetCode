from typing import List


class Solution:

    @staticmethod
    def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = list(map(lambda x: abs(x - 1), image[i]))[::-1]
        return image


print(Solution.flipAndInvertImage([[1, 1, 1], [1, 0, 1], [1, 1, 0]]))
