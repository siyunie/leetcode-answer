
# coding: utf-8

# In[ ]:


#7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# In[ ]:


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        f=1
        if x<0:
            x=-x
            f=-1
        a=x%10
        x=int(x/10)
        while x!=0:
            a*=10
            a+=x%10
            x=int(x/10)
        if a<2**31-1:
            return f*a
        else: return 0

