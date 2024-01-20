class Solution(object):
    def isHappy(self, n):
        while(len(str(n)) > 1):
            summa = 0
            for i in str(n):
                summa += int(i) ** 2
            n = summa

        if n == 1 or n == 7:
            return True
        else:
            return False        
        