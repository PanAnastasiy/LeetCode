class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dct = {chr(i + 64): i for i in range(1, 27)}
        print(dct)
        answer = 0
        l = len(columnTitle)
        for i in range(l):
            answer += dct[columnTitle[i]] * 26**(l-i-1)
            print(f'{dct[columnTitle[i]]}* 26^{l-i-1}')
        return answer


sol = Solution()
print(sol.titleToNumber("A"))
print(sol.titleToNumber("ZY"))
