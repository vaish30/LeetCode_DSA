class Solution:
    def reverseVowels(self, s: str) -> str:
        st = s.lower()
        st = list(s)
        dictionary = ['a','e','i','o','u','A','E','I','O','U']
        

        x, y = 0, len(st)-1

        while x<y:
            if st[x] in dictionary and st[y] in dictionary:
                st[x],st[y] = st[y],st[x]
                x+=1
                y-=1
            

            if st[x] not in dictionary:
                x+=1
            
            if st[y] not in dictionary:
                y-=1

            # print(s[x],s[y])            

        return "".join(st)
            
        