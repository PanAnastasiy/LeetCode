class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        data = {letter: magazine.count(letter) for letter in set(magazine)}
        for letter in ransomNote:
            if data.get(letter, 0):
                data[letter] -= 1
            else:
                return False
        if all(list(map(lambda x: x > -1, data.values()))):
            return True


sol = Solution()
print(sol.canConstruct('ayb', 'aayb'))
