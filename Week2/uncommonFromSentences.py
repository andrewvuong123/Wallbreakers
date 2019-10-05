class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        # General Idea: Have a dictionaries with the words from A and B and check for the word that appears only once.
        
        A_split = A.split()
        B_split = B.split()
        word_count = {}
        uncommon = []
        for word in A_split:
            if word not in word_count:
                word_count[word] = 1
            else: 
                word_count[word] += 1
        
        for word in B_split:
            if word not in word_count:
                word_count[word] = 1
            else: 
                word_count[word] += 1
        
        for word in word_count:
            if word_count[word] == 1:
                uncommon.append(word)
        return uncommon
            
            