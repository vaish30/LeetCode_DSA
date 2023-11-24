class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return False

        string = s.lower()
        
        new_string = ''

        new_string = new_string.join(i for i in string if i.isalnum())
        print(string, new_string)

        if new_string[::-1] == new_string:
            return True
            

        