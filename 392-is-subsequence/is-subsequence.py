class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        new_s = list(s)
        new_t = list(t)

        count = 0
        i, j = 0, 0
        while i < len(new_s) and j < len(new_t):
                if new_s[i] == new_t[j]:
                    i+=1
                j+=1
            
        if i == len(new_s):
            return True 
        else:
            return False
                
        