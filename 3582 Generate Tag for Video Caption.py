class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.strip()
        captions = caption.split(' ')
        words = [word.capitalize() for word in captions[1:]]
        answer = captions[0].lower() + ''.join(words)
        print(answer)
        for char in answer:
            if not char.isalpha():
                answer = answer.replace(char, '')
        return '#' + answer[:99]


print(Solution().generateTag("Leetcode daily streak achieved"))
print(Solution().generateTag("   "))
print(Solution().generateTag(" fPysaRtLQLiMKVvRhMkkDLNedQKffPnCjbITBTOVhoVjiKbfSawvpisDaNzXJctQkn"))