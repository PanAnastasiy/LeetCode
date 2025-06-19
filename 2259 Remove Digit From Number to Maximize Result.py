class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        answers = []
        for i in range(len(number)):
            if number[i] == digit:
                answers.append(number[:i] + number[i + 1:])
        return max(answers)
