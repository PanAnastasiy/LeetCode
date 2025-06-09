class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        letters = []
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)
        length_d = len(digits)
        length_l = len(letters)
        if abs(length_d - length_l) > 1:
            return ''
        answer = ''
        for i in range(min(length_l, length_d)):
            if length_d < length_l:
                answer += letters[i] + digits[i]
            else:
                answer += digits[i] + letters[i]
        if length_d < length_l:
            answer += letters[-1]
        elif length_d > length_l:
            answer += digits[-1]
        return answer


print(Solution().reformat('a0b1c2'))
