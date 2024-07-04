
class Solution(object):

    @staticmethod
    def lengthOfLongestSubstring(s):
        if len(set(s)) == len(s):
            return len(s)
        substrings = ['']
        for i in range(len(s)):
            substring = ''
            for j in range(i, len(s)):
                if s[j] not in substring:
                    substring += s[j]
                    substrings.append(substring)
                    continue
                break
        return len(max(substrings, key=len))


print(Solution.lengthOfLongestSubstring("asdfghjklzxcbn,.qwrtuo467"))
