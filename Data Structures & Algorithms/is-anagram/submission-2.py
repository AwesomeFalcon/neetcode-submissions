class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(not len(s) == len(t)): 
            return False
        smap = defaultdict()
        tmap = defaultdict()
        for i in range(len(s)):
            smap[s[i]] = smap.get(s[i], 0) + 1
            tmap[t[i]] = tmap.get(t[i], 0) + 1
        return smap == tmap