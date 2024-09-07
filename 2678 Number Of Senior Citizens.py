class Solution:
    def countSeniors(self, details: list[str]) -> int:
        total = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                total += 1
        return total


sol = Solution()
print(sol.countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
