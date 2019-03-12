
# coding: utf-8

# In[ ]:


#3.Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


# In[ ]:


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    def lengthOfLongestSubstring(self, s):
        current_length = max_length = start = 0
        seen = dict()
        for i, e in enumerate(s):
            if e in seen.keys() and seen[e] >= start:
                start = seen[e]
                current_length = i - seen[e]
            else:
                current_length += 1 
            seen[e] = i 
            max_length = max(current_length, max_length)
        return max_length

