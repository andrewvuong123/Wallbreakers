class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        # Idea: Split A and B into lists of words. Iterate through each list and add to a dictionary/hash map. Initialize each word to one and increment by one each time it appears. Return all keys of the hash that have value equal to one. 
        
        A_list, B_list = A.split(), B.split()
        word_hash = {}
        uncommon = []
        for word in A_list:
            if word not in word_hash:
                word_hash[word] = 1
            else:
                word_hash[word] += 1
        for word in B_list:
            if word not in word_hash:
                word_hash[word] = 1
            else:
                word_hash[word] += 1
        for word in word_hash:
            if word_hash[word] == 1:
                uncommon.append(word)
        return uncommon