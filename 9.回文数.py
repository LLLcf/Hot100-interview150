#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # # method 1
        # if x < 0:
        #     return False
        
        # else:
        #     new_x = str(x)
            
        #     for i in range(len(new_x)):
        #         if new_x[i] != new_x[len(new_x) - 1 - i]:
        #             return False
        
        #     return True
        
        # method2
        if x < 0:
            return False

        elif x == 0:
            return True
        
        else:
            if x % 10 == 0:
                return False
            
            new_num = 0
            while x > new_num:
                new_num = new_num * 10 + x % 10
                x = x // 10
            
            return x == new_num or x == new_num // 10
        
            
            

        
# @lc code=end

