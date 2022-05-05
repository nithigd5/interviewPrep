from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (n1 := head) and (n2 := head.next):
            n2.next, n1.next = n1, self.swapPairs(n2.next)
            return n2
        return head

        
def insert(h, l):
    t = h
    for i in l:
        t.next = ListNode(i) 
        t = t.next
    return h

l = [1,2,3,4,5]
h = ListNode(l[0])
h = insert(h, l[1:])
t = h
while t:
    print(t.val)
    t = t.next
Solution().swapPairs(h)
while h:
    print(h.val)
    h = h.next