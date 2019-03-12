
# coding: utf-8

# In[ ]:


#14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.


# In[ ]:


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is []:
            return ''
        shortest_str=min(strs,key=len)
        for i,ch in enumerate(shortest_str):
            for other_str in strs:
                if other_str[i]!=ch:
                    return shortest_str[:i]
        return shortest_str

