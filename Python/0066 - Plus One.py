class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.digits=digits
        r=0
        l=[]
        for i in digits:
            r=r*10+i

            
        r=r+1
        while r>0:
            d=r%10
            l.append(d)
            r=r//10
        
        l.reverse()
        return l
