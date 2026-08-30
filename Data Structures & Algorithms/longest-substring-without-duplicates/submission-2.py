class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = {}
        length = 0
        res = 0
        for i in range(len(s)):
            if s[i] in characters:
                length = max(length, characters[s[i]] + 1)
            characters[s[i]] = i
            res = max(res, i - length + 1)
        return res 