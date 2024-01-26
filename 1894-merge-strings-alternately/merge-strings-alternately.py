class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        merged_string = ''
        while i < len(word1) and j < len(word2):
            merged_string += word1[i]
            merged_string += word2[j]
            i+=1
            j+=1

        merged_string += word1[i:]
        merged_string += word2[j:]
        
        print(merged_string)
        return merged_string
       


        
        