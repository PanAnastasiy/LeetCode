class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                ...