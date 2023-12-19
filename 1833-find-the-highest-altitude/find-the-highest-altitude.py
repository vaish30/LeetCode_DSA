class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_num = 0
        cur_num = 0

        for i in range(len(gain)):
            if max_num < cur_num + gain[i]:
                max_num = cur_num + gain[i]

            cur_num += gain[i] 
        
        return max_num
    