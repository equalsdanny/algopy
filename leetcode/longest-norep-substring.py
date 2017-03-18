CHAR_SPACE=256

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        seen = [-1] * CHAR_SPACE
        maxlen = 1

        i = 0
        j = 0
        while i < n and j+1 < n:
            seen[ord(s[j])] = j

            j += 1
            last = seen[ord(s[j])]
            ok = last < i

            if ok:
                maxlen = max(maxlen, j - i + 1)
            else:
                i = last+1
        return maxlen

print(Solution().lengthOfLongestSubstring("pwwkew"))