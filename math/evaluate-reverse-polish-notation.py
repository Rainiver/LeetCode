class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        op = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)  # 向零截断
        }

        for item in tokens:
            if item in op:
                b, a = stack.pop(), stack.pop()  # b = right, a = left
                stack.append(op[item](a, b))
            else:
                stack.append(int(item))
        
        return stack.pop()
