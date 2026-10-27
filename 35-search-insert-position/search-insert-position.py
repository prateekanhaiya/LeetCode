class Solution(object):
    def searchInsert(self, nums, target):

        le = len(nums)
        
        for i in range(0,le) :
            if nums[i] >= target:
                return i
                
        return le

        