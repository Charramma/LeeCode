#!/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Charramma(Huang)
# @E-mail: huang.zyn@qq.com
# @Date: 2020/11/21 23:26
# @File: palindrome-number.py

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    result = s.isPalindrome(121)
    print(result)
