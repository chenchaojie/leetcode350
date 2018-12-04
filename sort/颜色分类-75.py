class Solution:
    # O(n2)
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, lens = 1, len(nums)
        while i < lens:
            j = i - 1
            value = nums[i]
            while j >= 0 and nums[j] > value:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = value
            i += 1

    def sortColors2(self, nums):
        d = {}
        for v in nums:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1

        i = 0
        for k, v in d.items():
            while v > 0:
                nums[i] = k
                i += 1
                v -= 1

    # 双指针算法　没想出来。。。
    def sortColors3(self, nums):
        low, higt, i = 0, len(nums) - 1, 0
        while i < higt:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                i += 1
                low += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[higt] = nums[higt], nums[i]
                i += 1
                higt -= 1



if __name__ == "__main__":
    l = [2, 0, 2, 1, 1, 0]
    Solution().sortColors3(l)
    print(l)
