#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dt = {}
        
        for i, num in enumerate(nums):
            
            if num in dt:
                return [dt[num], i]
            else:
                dt[target - num] = i
        
        return [-1, -1]
        
        
# @lc code=end

