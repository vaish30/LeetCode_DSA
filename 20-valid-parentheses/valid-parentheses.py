class Solution:
    def isValid(self, s: str) -> bool:

        # check whether the given string is valid or not 
        # so we have to create close to open hashkey
        # and we will use stack datastructure to store these strings and remove them



        hashmap = { ")" : "(", "]" : "[", "}" : "{" }

        stk = []

        for c in s:
            if c not in hashmap: #this gives the key from the hashmap
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[c]:
                        return False

        return not stk

            