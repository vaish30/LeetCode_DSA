class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #basecase
        if str1 + str2 != str2 +str1:
            return ""

        return str1[:gcd(len(str1),len(str2))] #finding the strings by slicing from beginning of the string omitting 0 till gcd
        
        
        
        
        
        
        
        
        
 