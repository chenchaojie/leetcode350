class Solution(object):
    # 这个代码的规律就是先连续的递减，在连续的递增
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        lens = len(height)

        # left, right = 0, 0
        ret = 0
        while i < lens:
            left = height[i]
            stack = []
            j = i + 1

            while j < lens and height[j - 1] >= height[j]:
                stack.append(height[j])
                j += 1
            if j < lens:
                while j + 1 < lens and height[j + 1] >= height[j]:
                    stack.append(height[j])
                    j += 1
                right = height[j]
                dst = right if right < left else left
                summ = len(stack) * dst
                # print(stack,dst)
                while stack:
                    v = stack.pop()
                    summ -= v if v < dst else dst
                ret += summ
            i = j

        return ret

    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        lens = len(height)

        # left, right = 0, 0
        ret = 0
        while i < lens:
            left = height[i]
            stack = []
            j = i + 1

            while j < lens and height[j] < left:
                stack.append(height[j])
                j += 1

            if j < lens:
                right = height[j]

                dst = right if right < left else left
                summ = len(stack) * dst
                # print(stack,dst)
                while stack:
                    v = stack.pop()
                    summ -= v if v < dst else dst
                ret += summ
            if height[j] >= left:
                i = j
            else:
                i += 1

        return ret


if __name__ == "__main__":
    print(Solution().trap2([4, 2, 3]))
