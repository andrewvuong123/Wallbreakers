class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # Make an initial array with values as none
        self.size = 100000
        self.array = [None] * self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        
        # If the index is empty at the key then form a list with the key as the value. If the index is not empty and has a list of keys, check to see if it exists, if it does continue, else add it to the list.
        if self.array[key] is None:
            self.array[key] = list([key])
        else:
            if key not in self.array[key]:
                self.array[key].append(key)
            

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        
        # If not empty check the list of keys for a match and then pop that value off the list.
        if self.array[key] is not None:
            for i in range(len(self.array[key])):
                if self.array[key][i] == key:
                    self.array[key].pop(i)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        # iterate through list of keys and if one matches then return true, else false.
        if self.array[key] is not None:
            for k in self.array[key]:
                if k == key:
                    return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)