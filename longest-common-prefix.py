#!/bin/env python3
# -*- coding utf-8 -*-
# @Author: Charramma(Huang)
# @E-mail: huang.zyn@qq.com
# @Time: 2020/12/4 20:29
# @File: longest-common-prefix.py
# @Software: Pycharm


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = list()
        strs = sorted(strs, key=lambda x: len(x))
        for key, value in enumerate(strs[0]):
            for st in strs:
                if st[key] != value:
                    break
            else:
                result.append(value)

        return "".join(result)


if __name__ == '__main__':
    li = ["dog", "racecar", "car"]
    s = Solution()
    result = s.longestCommonPrefix(li)
    print(result)
