class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[] for _ in range(n+1)]
        res[0] = [""]
        for i in range(n + 1):
            for j in range(i):
                for l in res[j]:
                    for r in res[i - j - 1]:
                        res[i].append("(" + l + ")" + r)
        return res[-1]