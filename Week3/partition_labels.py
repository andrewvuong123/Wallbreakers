class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # Idea: Traverse the reverse of the list and add every last index position of each letter to a dictionary with letter as the key. Then iterate the length of the string and keep variable pointers to the current letter's last index position and the overall max last index position. Take the max between the two and check if i reaches the max last index var. If it does we can append the index to the resulting list and then return the result at the end.
        reverse = "".join(reversed(S))
        last = {}
        result = []
        max_last = 0
        length = len(S) - 1
        
        for i, letter in enumerate(reverse):
            if letter not in last:
                last[letter] = length - i # append index from the end of original list
        
        for i in range(len(S)):
            curr = last[S[i]]
            max_last = max(curr, max_last)
            if i == max_last:
                result.append(i - sum(result)) # subtract the index from the previous partition to get the length of the new partition 
        result[0] += 1 # accounts for 0th indexing
        return result