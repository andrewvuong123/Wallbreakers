class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # General Idea: Have a hash map for each bill initialized and decrement/increment, if given 10 then need to have at least one five, if given 20 then need to have at least 15 (one 5 and one 10 or three 5s).
        
        money = {5: 0, 10: 0, 20: 0}
        
        for payment in bills:
            if payment == 5:
                money[payment] += 1
                
            elif payment == 10:
                if money[5] < 1:
                    return False
                money[payment] += 1
                money[5] -= 1
                
            elif payment == 20:
                if money[5] == 0 and money[10] > 1 or money[5] < 3 and money[10] == 0:
                    return False
                money[payment] += 1
                if money[10] < 1:
                    money[5] -= 3
                else:
                    money[10] -= 1
                    money[5] -= 1
        return True
                