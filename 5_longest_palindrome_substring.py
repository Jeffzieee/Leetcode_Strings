'''
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''


# Solution

def longestPalindrome(s: str) -> str:
    def expand(left, right, str, temp_flag, temp_flag_length):
        while left >= 0 and right < len(str) and str[left] == str[right]:
            if (right - left + 1) > temp_flag_length:
                temp_flag = str[left:right + 1]
                temp_flag_length = (right - left + 1)
            left -= 1
            right += 1

        return [temp_flag, temp_flag_length]

    flag = ""
    flag_length = 0

    for i in range(len(s)):
        flag, flag_length = expand(i, i, s, flag, flag_length)
        flag, flag_length = expand(i, i + 1, s, flag, flag_length)
    return flag


print(longestPalindrome("babad"))
