class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        answer = [first]
        for number in encoded:
            answer.append(answer[-1] ^ number)
        return answer


print(Solution().decode([1, 2, 3], 1))


