class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.array = [None] * self.size # initialize each cell to none for a fixed length size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key % self.size # key represents the index of the array
        hash_value = [key, value] # value in the array is the key value pair
        
        # If the value at the given key index is empty, add a new list containing the key value pair in it. Else iterate through the list at the index and if the key already exists, update the value, if it does not exist in the list, append it.
        if self.array[hash_key] is None:
            self.array[hash_key] = list([hash_value])
        else:
            for pairs in self.array[hash_key]:
                if pairs[0] == key:
                    pairs[1] = value
                    return
            self.array[hash_key].append(hash_value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        
        # Get hash key/index of the array. Iterate through the list of pairs at that index, if the key matches the given key then return the value in that pair, else return -1.
        
        hash_key = key % self.size
        if self.array[hash_key] is not None:
            for pair in self.array[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        
        # Get hash key/index of array, if at that index contains none don't do anything. Else loop through each item in the list at that index and pop the matching key value pair.
        hash_key = key % self.size
        if self.array[hash_key] is None:
            return
        for i in range(len(self.array[hash_key])):
            if self.array[hash_key][i][0] == key:
                self.array[hash_key].pop(i)
                return
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)