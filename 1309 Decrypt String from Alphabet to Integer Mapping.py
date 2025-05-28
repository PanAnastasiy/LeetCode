class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = []
        i = len(s) - 1
        while i > -1:
            if s[i] == '#':
                answer.append(chr(int(s[i-2: i]) + 96))
                i -= 3
                continue
            answer.append(chr(int(s[i]) + 96))
            i -= 1
        return ''.join(answer[::-1])


print(Solution().freqAlphabets("10#11#12"))
print(Solution().freqAlphabets("1326#"))
