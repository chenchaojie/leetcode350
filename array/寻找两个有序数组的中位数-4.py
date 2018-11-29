class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return 0
        if not nums1:
            return nums2[len(nums2) // 2]
        m1, m2 = min(nums1[0], nums2[0]), max(nums1[len(nums1) - 1], nums2[len(nums2) - 1])
        return (m1 + m2) / 2


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
