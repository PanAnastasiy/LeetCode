class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        dct = {a: chars.count(a) for a in set(chars)}
        answer = 0
        for word in words:
            for char in set(word):
                if char not in dct:
                    break
                if dct[char] < word.count(char):
                    break
            else:
                answer += len(word)
        return answer
