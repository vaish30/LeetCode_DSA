class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_list = dict()

        for i in nums:
            if i in freq_list:
                freq_list[i]+=1
            else:
                freq_list[i]=1

        top_freq = sorted(freq_list.items(), key=lambda i: i[1], reverse=True)
        sorted_dict = {key: value for key, value in top_freq}

        return list(sorted_dict.keys())[:k]

        
        