class Solution:

    def split_string(self, s):
        splited = []
        for i in range(0, len(s), 3):
            splited.append(s[i:i+3])
        return splited

    def thousandSeparator(self, n: int) -> str:
        answer = self.split_string(str(n)[::-1])
        return '.'.join(answer)[::-1]
