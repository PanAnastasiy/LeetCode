class Solution:
    '''
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        dct = dict.fromkeys(words, False)
        print(dct)
        for word in words:
            if word[::-1] in words and not dct[word[::-1]] and not dct[word] and len(set(word)) > 1:
                dct[word] = True
                dct[word[::-1]] = True
        print(dct)
        return len(list(filter(lambda x: x, dct.values()))) // 2
    '''

    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        s = set()
        ans = 0
        for word in words:
            if word[::-1] in s:
                ans += 1
            else:
                s.add(word)
        return ans



print(Solution().maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]))
print(Solution().maximumNumberOfStringPairs(["ab", "ba", "cc"]))
