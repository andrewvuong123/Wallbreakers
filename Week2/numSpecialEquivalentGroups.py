class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # General Idea: For each string create a new string by separating the even/odd indices and then sort and merge them back together. Then we can add the unique new strings into a set and return the length of the set.
        
        result = set()
        for string in A:
            odd = "".join(sorted(string[1::2]))
            even = "".join(sorted(string[0::2]))
            result.add(even + odd)
        return len(result)   
            
            