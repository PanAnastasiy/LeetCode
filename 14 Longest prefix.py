
class Solution:

    @staticmethod
    def longestCommonPrefix(strs):
        answer = ""
        for letter in min(strs, key=len):
            answer += letter
            if not all([True if answer == word[:len(answer)] else False for word in strs]):
                return answer[:-1]
        return answer


print(Solution.longestCommonPrefix(["flower", "flow", "flight"]))
