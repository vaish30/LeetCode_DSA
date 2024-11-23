class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)

        arr = []
        for n,c in count.items():
            arr.append([c, n])
        arr.sort()
        print(arr)

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        # print(arr)


'''

        
        for n, c in count.items():
                freq[c].append(n)

        res = []
        for i in range(len(freq) -1, 0 , -1):
            for j in  freq[i]:
                res.append(j)
                if len(res) == k:
                    return res'''
