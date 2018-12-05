class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s, e = 0, x
        while s <= e:
            mid = (s + e) // 2
            if mid ** 2 > x:
                e = mid - 1
            elif mid ** 2 < x:
                if (mid + 1) ** 2 > x:
                    return mid
                s = mid + 1
            else:
                return mid


if __name__ == "__main__":
    print(Solution().mySqrt(10))
