class Solution:
    def isPalindrome_str(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
    def isPalindrome(self, x:int) -> bool:
        rev = 0
        temp = x
        while (x>0):
            rem = x % 10
            rev = rev * 10 + rem
            x = x//10
        
        return temp == rev
            

        