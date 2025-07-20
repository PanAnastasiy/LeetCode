class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        answer = 0
        if set(s1) != set(s2):
            return False
        ch1 = set()
        ch2 = set()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                answer += 1
                ch1.add(s1[i])
                ch2.add(s2[i])
        if ch1 != ch2:
            return False
        return answer in [0, 2]
