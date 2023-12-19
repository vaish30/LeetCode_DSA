class Solution(object):
    def uniqueOccurrences(self, arr):
        hash = {}
        for num in arr:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        seen_values = set()
        bool1 = True

        for key, value in hash.items():
            if value in seen_values:
                bool1 = False
                break
            seen_values.add(value) 
        return bool1


        """
        :type arr: List[int]
        :rtype: bool
        """
        