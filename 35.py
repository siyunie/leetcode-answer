
# coding: utf-8

# In[ ]:


#35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0


# In[ ]:


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        elif nums[0]>target:
            return 0
        elif nums[-1]<target:
            return len(nums)
        else:
            for i in range(len(nums)-1):
                if nums[i]<target and nums[i+1]>=target:
                    return i+1
                

