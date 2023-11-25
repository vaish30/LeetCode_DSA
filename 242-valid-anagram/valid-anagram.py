#get count for each letter in s and t 
# compare it with 


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        # for i in t:
        #     s_dict[i] = s_dict.get(i,0) - 1

        # for i in s_dict:
        #     if s_dict[i] != 0:
        #         return False
        # return True 


        for i in s:
            s_dict[i] = s_dict.get(i,0) + 1

        for i in t:
            t_dict[i] = t_dict.get(i,0) + 1

        print(s_dict, t_dict)

        return s_dict == t_dict




