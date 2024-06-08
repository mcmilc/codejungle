"""Leetcode 88 problem

Merge sorted array.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        max_i = m
        self._error_check(nums1, m, nums2, n)
        for k in range(n + m):
            if i < max_i and j < n:
                if nums1[i] <= nums2[j]:
                    i += 1
                else:
                    for _l in range(max_i - 1, i - 1, -1):
                        nums1[_l + 1] = nums1[_l]
                    nums1[i] = nums2[j]
                    i += 1
                    j += 1
                    max_i += 1
            elif i == max_i and j < n:
                nums1[k] = nums2[j]
                j += 1

    def _error_check(self, nums1, m, nums2, n):
        total_len = n + m
        max_val = 10**9

        if m < 0 or m > 200 or n < 0 or n > 200:
            return None

        if total_len < 1 or total_len > 200:
            return None

        for i in nums1:
            if i < -max_val or i > max_val:
                return None

        for i in nums2:
            if i < -max_val or i > max_val:
                return None


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 4, 10, 0, 0, 0, 0]
    nums2 = [2, 3, 5, 6]
    s.merge(nums1, 4, nums2, 4)
    print(nums1)
    nums1 = [2, 3, 5, 6, 0, 0, 0, 0]
    nums2 = [1, 2, 4, 10]
    s.merge(nums1, 4, nums2, 4)
    print(nums1)
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    print(nums1)
