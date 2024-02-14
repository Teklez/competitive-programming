# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        current = head
        while current:
            current = current.next
            count += 1
        quo = count // k
        rem = count % k

        curr = head
        i = 0
        res = []
        while curr and i <= count:
            print(rem)
            add = 1 if rem > 0 else 0
            rem -= 1 if rem > 0 else 0
            ci = i
            res.append(curr)
            while i < ci + quo + add - 1:
                if curr:
                    curr = curr.next
                i += 1
            if curr:
                nxt = curr.next
                curr.next = None
                curr = nxt
            i += 1
        if k > count:
            for _ in range(k - count % k):
                res.append(None)
        return res

        
            




        