class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        self.list1=list1
        self.list2=list2
        
        arr=[]
        while list1:
            arr.append(list1.val)
            list1=list1.next
        
        arr2=[]
        while list2:
            arr2.append(list2.val)
            list2=list2.next
        
        for i in arr2:
            arr.append(i)
        
        arr.sort()
            
        dummy = ListNode(0)
        current = dummy

        for i in arr:
            current.next = ListNode(i)
            current = current.next

        return dummy.next
                
