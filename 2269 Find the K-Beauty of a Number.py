class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        answer = 0
        s = str(num)
        for i in range(0, len(s) - k + 1):
            divisor = int(s[i:i+k])
            print(divisor)
            if divisor and num % divisor == 0:
                answer += 1
        return answer


print(Solution().divisorSubstrings(430043, 2))
print(Solution().divisorSubstrings(240, 2))