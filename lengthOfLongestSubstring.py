class Solution(object):
    def lengthOfLongestSubstring(self, s):
        x = ''
        max_len = 0

        for ch in s:
            if ch in x:
                x = x[x.index(ch) + 1:]  # remove till duplicate

            x += ch
            max_len = max(max_len, len(x))

        return max_len
