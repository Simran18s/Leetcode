class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        res = ""
        for r in range(numRows):
            ic = 2*(numRows - 1)
            for i in range(r, len(s), ic):
                res += s[i]
                if (r>0 and r < numRows -1 and i + ic - 2*r < len(s)):
                    res += s[i + ic - 2*r]
        return res
