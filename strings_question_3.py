'''
QUESTION!!!

Given a string s, find the length of the longest 
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''

# SOLUTION !

def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    temp = set()
    left = 0
    flag = 0

    for right in range(n):
        if s[right] not in temp:
            temp.add(s[right])
            flag = max(flag, right - left + 1)

        else:
            while s[right] in temp:
                temp.remove(s[left])
                left += 1
            temp.add(s[right])

    return flag