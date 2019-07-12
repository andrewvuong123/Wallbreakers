import bisect 
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Idea: Sort pattern p and then iterate through the string s by a sliding window. Sort each window and if it matches append the index to a list.
        result = []
        pattern, string = list(p), list(s)
        pattern.sort()
        window = string[0:len(p)] #sliding window
        window.sort()
        stop = len(s) - len(p) - 1 # stop before window goes out of range based on pattern length
        for i, letter in enumerate(s):
            if window == pattern: 
                result.append(i)
            if i > stop:
                break
            else:
                window.pop(window.index(letter)) # remove the first letter from window 
                bisect.insort(window, s[i+len(p)]) # use the bisect method to insert the next letter of the list into the window at the sorted spot        
        return result
            
            
            
    