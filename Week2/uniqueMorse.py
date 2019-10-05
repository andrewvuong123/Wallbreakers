class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # General Idea: Create a dictionary mapping the alphabet to morse code and then iterate/concatenate the transformation of the words and add it to a set.
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        translate = {}
        result = set()
        for i, letter in enumerate(alpha):
            translate[letter] = morse[i]
            
        for word in words:
            string = ""
            for letter in word:
                string = string + translate[letter]
            result.add(string)
        return len(result)
            
                
                