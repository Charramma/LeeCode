class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # pre = 1
        # y = 0
        # if x < 0:
        #     x = abs(x)
        #     pre = -1
        # while x != 0:
        #     y = y * 10 + x % 10
        #     x = x // 10
        # return pre * y
        x = list(str(x))
        x.reverse()
        if x[-1] == '-':
            del x[-1]
            x.insert(0, '-')
        return int("".join(x))


if __name__ == '__main__':
    s = Solution()
    result = s.reverse(-123)
    print(result)
