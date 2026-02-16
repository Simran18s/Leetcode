import re

class Solution(object):
    def isMatch(self, s, p):
        return re.match("^" + p + "$", s) is not None
