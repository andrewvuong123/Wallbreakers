class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # Idea: Use a dictionary/hash map to map the pattern as the key to the str as the value. Then check if the key in the dictionary matches each str at its corresponding index. Do the same process but using str as the key and pattern as the value.
        
        if not pattern or not str or len(pattern) != len(str.split()):
            return False
        pattern_dict = {}
        str_dict = {}
        str_list = str.split() # to split string into list of words
        for i, letter in enumerate(pattern):
            pattern_dict[letter] = str_list[i]
        for i, word in enumerate(str_list):
            str_dict[word] = pattern[i]
            
        for i, letter in enumerate(pattern):
            if pattern_dict[letter] != str_list[i]:
                return False
        for i, word in enumerate(str_list):
            if str_dict[word] != pattern[i]:
                return False
        
        return True
        