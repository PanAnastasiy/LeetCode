class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        data = {}
        for letter in licensePlate.lower():
            if letter.isalpha():
                data[letter] = data.get(letter, 0) + 1
        print(data)
        for word in sorted(words, key=len):
            for key in data:
                if word.count(key) < data[key]:
                    break
            else:
                return word


sol = Solution()
print(sol.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]))
