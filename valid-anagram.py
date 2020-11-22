#!/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Charramma(Huang)
# @E-mail: huang.zyn@qq.com
# @Date: 2020/11/22 21:26
# @File: valid-anagram.py

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

if __name__ == '__main__':
    s = Solution()
    str1 = "anagram"
    str2 = "nagaram"
    result = s.isAnagram(str1, str2)
    print(result)
