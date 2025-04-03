class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first_pointer = 0
        second_pointer = 0
        answer = []
        while first_pointer < len(word1) and second_pointer < len(word2):
            answer.append(word1[first_pointer] + word2[second_pointer])
            first_pointer += 1
            second_pointer += 1

        while first_pointer < len(word1):
            answer.append(word1[first_pointer])
            first_pointer += 1

        while second_pointer < len(word2):
            answer.append(word2[second_pointer])
            second_pointer += 1
        return ''.join(answer)


print(Solution().mergeAlternately("word1", "word2"))
