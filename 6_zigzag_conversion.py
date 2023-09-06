'''
QUESTION

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''

#SOLUTION

def convert( s: str, numRows: int) -> str:
    flag_list = [[] for rows in range(numRows)]
    flag = ""
    index = 0
    oscillator = 1

    if numRows == 1 or numRows >= len(s):
        flag = s
        return flag

    for char in s:

        flag_list[index].append(char)

        if index == 0:
            oscillator = 1
        elif index == numRows - 1:
            oscillator = -1
        index += oscillator

    for row in range(numRows):
        flag_list[row] = ''.join(flag_list[row])

    flag = ''.join(flag_list)

    return flag

print(convert("PAYPALISHIRING",3))