class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        res=[]
        ln=ceil(intLength/2)
        odd=intLength%2==1
        base=10**(ln-1)
        def getLalindrome(k:int)->int:
            val=str(k-1+base)
            if len(val)>ln:
                return -1
            return int(val+val[-2::-1]) if odd else int(val+val[::-1])
        for q in queries:
            res.append(getLalindrome(q))  
        return res 