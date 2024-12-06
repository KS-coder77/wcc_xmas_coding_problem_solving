# Problem 28. Find the Index of the First Occurrence in a String:
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1
