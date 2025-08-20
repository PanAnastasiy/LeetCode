class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)[2:].lstrip('1')
        print(n)
        answer = 0
        for i in range(len(n)):
            if n[i] == '0':
                answer += 2**(len(n) - i - 1)
        return answer


print(Solution().bitwiseComplement(5)) # 2
print(Solution().bitwiseComplement(7)) # 0
print(Solution().bitwiseComplement(10)) # 5
