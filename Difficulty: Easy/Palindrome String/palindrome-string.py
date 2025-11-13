class Solution:
    def isPalindrome(self, s):
        # code here
        reversed_string = ''.join(reversed(s))
        if s==reversed_string:
            return True
        else:
            return False
