class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        symbols = [s[:len(s) % k]] if len(s) % k else []
        for i in range(len(s) % k, len(s), k):
            symbols.append(s[i:i + k])
        return '-'.join(symbols)


print(Solution().licenseKeyFormatting(s="5F3Z-2e-9-w", k=4))
print(Solution().licenseKeyFormatting(s="2-5g-3-J", k=2))
