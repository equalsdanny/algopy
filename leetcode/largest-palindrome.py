class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            now = False
            for j in range(len(s)-1,-1,-1):
                if s[i] == s[j]:
                    now = True