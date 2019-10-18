class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # General Idea: Can use the dynamic edit distance algorithm to solve, create a 2d table to sovle.
        m = len(word1)
        n = len(word2)
        E = [[0 for x in range(n+1)] for x in range(m+1)] # initialize table with 0s
        
        for i in range(m+1):
            for j in range(n+1):
                # Base cases, if second string is empty then remove all characters of second str, if first string is empty, insert all characters of second string
                if j == 0:
                    E[i][j] = i
                elif i == 0:
                    E[i][j] = j
                # Case where the letter is the same at the last character, ignore and recur on rest   
                elif word1[i-1] == word2[j-1]:
                    E[i][j] = E[i-1][j-1]
                else:
                    E[i][j] = 1 + min(E[i-1][j], E[i][j-1], E[i-1][j-1])
        
        return E[m][n]    