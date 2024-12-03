# Problem 14. Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # set the first string as the prefix
        comm_pf = strs[0]

        for string in strs[1:]:
            while not string.startswith(comm_pf):
                # reduce the prefix length until it matches the current string
                comm_pf = comm_pf[:-1]
                if not comm_pf:
                    return ""

        return comm_pf
