class Solution:
    def reverseWords(self, s: str) -> str:
        new_string = s.strip().split() #removes all trailing spaces

        output = ""

        for i in range(len(new_string)-1,0,-1):
            output += new_string[i] + " "

        return output + new_string[0]
        