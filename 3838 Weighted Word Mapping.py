from string import ascii_lowercase


class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        d = dict(zip(ascii_lowercase, weights))
        result = ''
        for word in words:
            counter = 0
            for char in word:
                counter += d[char]
            result += ascii_lowercase[::-1][counter % 26]
        return result


print(Solution().mapWordWeights(words = ["abcd","def","xyz"],
                                weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))

print(Solution().mapWordWeights(words=["a", "b", "c"],
                                weights=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))