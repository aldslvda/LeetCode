'''
318. Maximum Product of Word Lengths
Description  Submission  Solutions
Total Accepted: 44185
Total Submissions: 103279
Difficulty: Medium
Contributors: Admin
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''
class Solution(object):
    def maxProduct(self, words):
        d = {}
        for w in words:
            tmp = 0x0
            for ch in set(w):
                tmp |= (0x1 << (ord(ch) - 97))
            d[tmp] = max(d.get(tmp, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
