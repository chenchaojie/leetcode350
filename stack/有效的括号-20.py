class Solution(object):
    # 利用哨兵，简化逻辑条件　O(n)
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            "(": ")",
            "{": "}",
            "[": "]",
            "#": "#"
        }

        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            else:
                val = stack.pop() if stack else "#"
                if c != d[val]:
                    return False

        return not stack

    def isValid2(self, s):
        pass


if __name__ == "__main__":
    print(Solution().isValid("}"))
