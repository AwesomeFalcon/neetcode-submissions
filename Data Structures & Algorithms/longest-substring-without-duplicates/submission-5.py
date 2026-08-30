class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        currLength = 0
        characters = {}
        for i in range(len(s)):
            if s[i] in characters:
                currLength = max(characters[s[i]] + 1, currLength)
            characters[s[i]] = i
            length = max(length, i - currLength + 1)
        return length