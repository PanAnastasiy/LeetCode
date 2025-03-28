class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        answer = []
        for letter in range(ord(s[0]), ord(s[3]) + 1):
            for number in range(int(s[1]), int(s[-1]) + 1):
                answer.append(chr(letter) + str(number))
        return answer


print(Solution().cellsInRange("K1:L2"))
print(Solution().cellsInRange("A1:F1"))
