class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # dictionary/hash mapping letter keys to morse code values
        a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse = {}
        for i, letter in enumerate(a):
            morse[letter] = m[i]
        
        # transform each letter into morse code/concatenate
        transformation = []
        # contains only unique values
        result = set() 
        for word in words:
            for letter in word:
                transformation.append(morse[letter])
            result.add(''.join(transformation))
            transformation = [] # reset list after each word concatenation
            
        return len(result)
        