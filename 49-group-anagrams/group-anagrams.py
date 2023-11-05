class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for i in strs:
            sorted_keys = "".join(sorted(i))

            if sorted_keys not in anagram_dict:
                anagram_dict[sorted_keys]=[]

            anagram_dict[sorted_keys].append(i)

        anagram_group = list(anagram_dict.values())[::-1]
        return anagram_group
           