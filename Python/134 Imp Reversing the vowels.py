'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"


Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".



Example 2:

Input: s = "leetcode"

Output: "leotcede"'''




class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")  # Use a set for faster lookup
        s = list(s)  # Convert string to list since strings are immutable
        i, j = 0, len(s) - 1  # Two-pointer approach

        while i < j:
            while i < j and s[i] not in vowels:  # Move left pointer to a vowel
                i += 1
            while i < j and s[j] not in vowels:  # Move right pointer to a vowel
                j -= 1
            if i < j:  # Swap vowels
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)  # Convert list back to string
