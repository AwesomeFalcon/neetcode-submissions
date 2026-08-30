class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        for i in tokens:
            if i in ops:
                first = int(stack[-1])
                stack.pop()
                second = int(stack[-1])
                stack.pop()
                if i == "+":
                    stack.append(first + second)
                    print("adding", first, second)
                if i == "-":
                    stack.append(second - first)
                    print("subtracting", second, first)
                if i == "*":
                    stack.append(first * second)
                    print("multiplying", first, second)
                if i == "/":
                    stack.append(math.trunc(second / first))
                    print("dividing", second, first)
            else:
                stack.append(i)
                print("appending", i)
        print(stack)
        return int(stack[-1])