class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        maxf = 0
        for r, ch in enumerate(s):
            count[ch] += 1
            maxf = max(maxf, count[ch])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return len(s) - l