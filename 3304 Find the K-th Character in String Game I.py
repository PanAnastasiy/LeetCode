class Solution:

    def kthCharacter(self, k: int) -> str:
        answer = 'a'

        def generate(s: str) -> str:
            result = ''
            for char in s:
                result += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            return result

        while len(answer) < k:
            answer += generate(answer)
        return answer[k - 1]


print(Solution().kthCharacter(5))
