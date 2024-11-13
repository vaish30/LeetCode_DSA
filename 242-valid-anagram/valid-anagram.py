class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h_s, h_t = {}, {} #multiple assignment

        for i in range( len(s)):
            h_s[s[i]] = 1 + h_s.get(s[i],0)
            h_t[t[i]] = 1 + h_t.get(t[i],0)

        print(h_s)
        print(h_t)

        for c in h_s:
            if h_s[c] != h_t.get(c,0):
                return False
                
        return h_s == h_t



        