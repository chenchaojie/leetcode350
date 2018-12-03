class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        def calc(val1, val2, op):
            print(val1,val2,op)
            if op == '+':
                return val1 + val2
            elif op == '-':
                return val1 - val2
            elif op == '*':
                return val1 * val2
            elif op == '/':
                if val2 == 0:
                    return 0
                return int(val1 / val2)

        s = []
        ops = set(['*', '+', '-', '/'])
        for v in tokens:
            if v not in ops:
                s.append(int(v))
            else:
                # print(v)
                val2, val1 = s.pop(), s.pop()
                s.append(calc(val1, val2, v))

        return s.pop()


if __name__ == "__main__":
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
