class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(chars) for chars in s.split() if chars.isnumeric()]
        for i in range(1, len(numbers)):
            if numbers[i] <= numbers[i-1]:
                return False
        return True
