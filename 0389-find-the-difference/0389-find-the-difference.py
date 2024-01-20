class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = {}
        
        # Count characters in string t
        for char in t:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Subtract characters in string s
        for char in s:
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        
        # The remaining character in char_count is the difference
        return list(char_count.keys())[0]