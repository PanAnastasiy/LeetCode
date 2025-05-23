class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        dct = {}
        for response in responses:
            for answer in set(response):
                dct[answer] = dct.get(answer, 0) + 1
        print(dct)
        return min(dct.keys(), key=lambda x: (-dct.get(x), x))


print(Solution().findCommonResponse([["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]))