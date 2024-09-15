class Solution:
    def convertDateToBinary(self, date: str) -> str:
        numbers = list(map(int, date.split('-')))
        return '-'.join([bin(number)[2:] for number in numbers])


sol = Solution()
print(sol.convertDateToBinary("2080-02-29"))
