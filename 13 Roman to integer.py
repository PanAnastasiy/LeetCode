from functools import reduce


class Solution:

    @staticmethod
    def romanToInt(s):
        translater, roman, i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                                'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}, [], 0
        while i < len(s):
            if s[i: i + 2] not in translater.keys():
                roman.append(s[i])
                i += 1
            else:
                roman.append(s[i:i + 2])
                i += 2
        return reduce(lambda x, y: x + y, map(lambda x: translater[x], roman), 0)


print(Solution.romanToInt("MCMXCIV"))
