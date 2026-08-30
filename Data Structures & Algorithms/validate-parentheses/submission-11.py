class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] == "(" and i != ")" or stack[-1] == "{" and i != "}" or stack [-1] == "[" and i != "]":
                    return False
                stack.pop()
        if not stack:
            return True
        else:
            return False