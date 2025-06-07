class Solution:
    def dayOfYear(self, date: str) -> int:
        answer = 0
        dct = {
               1: 31,
               2: 28,
               3: 31,
               4: 30,
               5: 31,
               6: 30,
               7: 31,
               8: 31,
               9: 30,
               10: 31,
               11: 30,
               12: 31
               }
        year, month, day = map(int, date.split('-'))
        print(year, month, day)
        for mon in range(month - 1):
            answer += dct[mon + 1]
            print(answer)
        if month > 2:
            answer += year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        print(answer)
        answer += day
        return answer


print(Solution().dayOfYear("2019-01-09")) #9
print(Solution().dayOfYear("2019-02-10")) #41
print(Solution().dayOfYear("2004-03-01")) #61
