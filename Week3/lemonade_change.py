class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # Idea: Create a hash map to 5/10/20 dollar bills and then use conditionals to check if the cases are satisfied.
        change = {5: 0, 10: 0, 20:0}
       
        for money in bills:
            change[money] += 1
            
            if money == 5:
                continue
                
            # check for 10
            elif money == 10:
                if change[5] == 0:
                    return False
                change[5] -= 1
                
            # check for 20
            elif money == 20:
                if  change[10] > 0 and change[5] == 0 or change[5] < 3 and change[10] == 0:
                    return False
                if change[10] > 0:
                    change[10] -= 1
                    change[5] -= 1
                else:
                    change[5] -= 3
        return True