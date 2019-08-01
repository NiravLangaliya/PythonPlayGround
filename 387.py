"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

class Solution(object):

    def firstUniqChar(self, s):
        uniq_dict=dict()
        for i in s:
            if uniq_dict.has_key(i):
                uniq_dict[i]=uniq_dict[i]+1
            else:
                uniq_dict[i] =1
        for ch in s:
            if uniq_dict[ch] == 1:
                return (s.index(ch),ch)



S = Solution()
result=S.firstUniqChar('loveleetcode')
print (result)