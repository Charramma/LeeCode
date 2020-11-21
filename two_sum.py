#!/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Charramma(Huang)
# @E-mail: huang.zyn@qq.com
# @Date: 2020/11/21 22:22
# @File: two_sum.py

class Solution(object):
    def twoSum(self, nums: list, target: int):
        result = list()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target and i not in result and j not in result:
                        result.append(i)
                        result.append(j)
        return result


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    s = Solution()
    result = s.twoSum(nums, target)
    print(result)