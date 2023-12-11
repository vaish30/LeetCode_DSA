class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)  # Convert the string to a list of characters
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        first, second = 0, len(string) - 1

        while first < second:
            if string[first].lower() in vowels and string[second].lower() in vowels:
                # Swap characters
                string[first], string[second] = string[second], string[first]
                first += 1
                second -= 1

            # Move the pointers if the characters are not vowels
            if string[first].lower() not in vowels:
                first += 1
            if string[second].lower() not in vowels:
                second -= 1

        return "".join(string)  # Convert the list of characters back to a string
