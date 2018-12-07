class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []

        def subfunc(str, left, right):
            if not left and not right:
                ret.append(str)

            if left:
                subfunc(str + "(", left - 1, right)
            if right and right > left:
                subfunc(str + ")", left, right - 1)

        subfunc("", n, n)
        return ret


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
