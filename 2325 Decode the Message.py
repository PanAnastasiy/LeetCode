from string import ascii_lowercase


class Solution(object):

    def decodeMessage(self: str, key: str, message: str) -> str:
        keys = []
        for ch in key.replace(' ', ''):
            if ch not in keys:
                keys.append(ch)
        d = dict(zip(keys, ascii_lowercase))
        d[' '] = ' '
        answer = [d[ch] for ch in message]
        return ''.join(answer)


sol = Solution()
print(sol.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
print(sol.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))