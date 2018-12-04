class Solution:
    # 解不出来　看答案
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        i = 0
        lens = len(nums)
        while i < lens:
            j = 0
            while j < lens - i - 1:
                if compare(str(nums[j]), str(nums[j + 1])):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j += 1
            i += 1
        i = lens - 1
        ret = ''
        while i >= 0:
            ret += str(nums[i])
            i -= 1
        return ret


def compare(astr, bstr):
    '''

    :param str a:
    :param str b:
    :return:
    '''

    lens = len(astr) if len(astr) > len(bstr) else len(bstr)
    i = 0
    pa, pb = astr[len(astr) - 1], bstr[len(bstr) - 1]
    while i < lens:
        if i >= len(astr):
            a = pa
        else:
            a = astr[i]

        if i >= len(bstr):
            b = pb
        else:
            b = bstr[i]
        # 逻辑错误
        # print(a,b,i,len(a),len(b))
        if int(a) > int(b):
            # print(a,b)
            return True
        elif int(b) > int(a):
            return False
        i += 1
    return True


if __name__ == "__main__":
    # print(compare(str(128), str(16)))
    print(Solution().largestNumber([1,2,4,8,16,32,64,128,256,512]))
