class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        answer = []
        for index, height in enumerate(mountain):
            if index in (0, len(mountain) - 1):
                continue
            if mountain[index - 1] < height and height > mountain[index + 1]:
                answer.append(index)
        return answer