#!/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Charramma(Huang)
# @E-mail: huang.zyn@qq.com
# @Date: 2020/11/22 14:55
# @File: palindrome-number-v2.py

class Solution(object):
    def isPalindrome(self, x):
        s = x
        y = 0
        while s > 0:
            y = y * 10 + s % 10
            s = s // 10
        if x == y:
            return True
        else:
            return False



if __name__ == '__main__':
    s = Solution()
    # li = [121, 123, -121]
    li = [121, 123, 686, -123, -121, 1221]
    result = list()
    for i in li:
        result.append(s.isPalindrome(i))
    print(result)
