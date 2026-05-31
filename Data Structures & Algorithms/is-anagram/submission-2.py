class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        # This counts the number of char in a string (s) inside the counter dictionary.
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        # This will decrease the counter from string (s) based on the string (t) and check if anagram
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        # Will return True if conditions met
        return True