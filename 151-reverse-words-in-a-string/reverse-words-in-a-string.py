class Solution:
    def reverseWords(self, s: str) -> str:
        # print(s.strip())
        new_s = s.strip().split()
        # print(new_s)

        return " ".join(new_s[::-1])