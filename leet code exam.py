'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0'''
#program:
class Solution:
    def addDigits(self, num: int) -> int:
        if num==0 or num%9!=0:
            return num%9
        else:
            return 9
#2)
'''Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        while True:
            return str(x) == str(x)[::-1]
 '''You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.

 

Example 1:

Input: n = 7
Output: 6
Explanation: Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.
Example 2:

Input: n = 14
Output: 13
Explanation: Details of the tournament:
- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 7 + 3 + 2 + 1 = 13.'''
 class Solution:
    def numberOfMatches(self, n: int) -> int:
        m=0
        while n>1:
            if n%2==0:
                m=m+(n/2)
                n=n/2
            else:
                 m=m+((n-1)/2)
                 n=(n-1)/2+1
        return int(m)
