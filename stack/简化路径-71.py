class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i = 0
        l = len(path)
        # stack.append('/')
        while i < l and path[i] == '/':
            i += 1

        while i < l:
            s = i
            while i < l and path[i] != '/':
                i += 1
            s1 = path[s:i]
            if s1 == '..':
                if stack: stack.pop()
            elif s1 != '.':
                stack.append(s1)
            while i < l and path[i] == '/':
                i += 1
        ret = ""
        while stack:
            val = stack.pop()
            ret = val + '/' + ret

        return '/' + ret[:len(ret) - 1]


if __name__ == "__main__":
    print(Solution().simplifyPath("/.."))
