from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return []

        s_chars = set(s)
        w_chars = set()
        for w in wordDict:
            w_chars |= set(w)

        if len(s_chars - w_chars) > 0:
            return []

        word_lens = [len(w) for w in wordDict]
        max_len = max(word_lens)
        min_len = min(word_lens)
        word_set = set(wordDict)

        options = self.find(s, min_len, max_len, word_set, [])
        return [
            ' '.join(s)
            for s in options
        ]


    def find(self, s, min_len, max_len, word_set, sentence):
        if len(s) == 0:
            return [sentence]

        # if s in self.cache:
        #     return self.cache[s]

        options = []
        for end in range(min_len, min(max_len, len(s))+1):
            sub = s[:end]
            if sub in word_set:
                options += self.find(
                    s[end:],
                    min_len,
                    max_len,
                    word_set,
                    sentence + [sub]
                )

        # self.cache[tuple(sentence)] = options
        return options

print(Solution().wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
print(Solution().wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))

print(Solution().wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
print(Solution().wordBreak(s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]))

print(Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
))

print(Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
))
