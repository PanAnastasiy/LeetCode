class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        length_s = []
        for i in range(len(s)):
            length_s.append(widths[ord(s[i]) - 97])
        print(length_s)
        lines = 0
        index = 0
        i = 0
        while i < len(s):
            if sum(length_s[index:i + 1]) <= 100:
                i += 1
                continue
            else:
                lines += 1
                index = i
                i -= 1
        return [lines + 1, sum(length_s[index:])]


print(Solution().numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa"))
print(Solution().numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"abcdefghijklmnopqrstuvwxyz"))