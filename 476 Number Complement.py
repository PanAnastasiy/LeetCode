class Solution:
    def findComplement(self, num: int) -> int:
        n = bin(num)[2:].lstrip('1')
        answer = 0
        for i in range(len(n)):
            if n[i] == '0':
                answer += 2**(len(n) - i - 1)
        return answer
