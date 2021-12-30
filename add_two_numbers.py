# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        carry=0
        Lexist=False
        while(l1 and l2):
            sval=l1.val+l2.val+carry
            if(sval<10 and Lexist==False):
                ansNode=ListNode(sval)
                Lexist=True
                carry=0
            elif(sval<10):
                ansNode.next=ListNode(sval)
                carry=0
            elif(Lexist==False and sval>=10):
                carry=1
                ansNode=ListNode(sval%10)
                Lexist=True
            else:
                carry=1
                ansNode.next=ListNode(sval%10)
                
            l1.next
            l2.next
        while(l1.next):
            ansNode.next=ListNode(l1.val)
        while(l2.next):
            ansNode.next=ListNode(l2.val)
            
        return ansNode

print(Solution().addTwoNumbers([2,4,3],[5,6,4]))