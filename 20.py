
# coding: utf-8

# In[ ]:


#20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true


# In[ ]:


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping_dict = {')':'(','}':'{',']':'['}
        
        for each_char in s:
            if each_char not in mapping_dict:
                stack.append(each_char)
            elif not stack or stack.pop() != mapping_dict[each_char]:
                return False
        return not stack

