# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# integer array = nums =[] (sorted in increasing order)
# remove the duplicates in-place
# relative order should be kept the same
# return k - the number of unique elems in variable nums

class Solution(object):
    def removeDuplicates(self, nums):
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1
