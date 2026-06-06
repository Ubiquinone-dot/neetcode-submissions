# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Traverse the head list, comparing each element to list2
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            # iterate
            cur = cur.next
        
        # Whichever dropped out set that as remainder
        cur.next = list1 if list1 is not None else list2

        return dummy.next


        # head = list1
        # comp = list2

        # while True:
            
        #     if head.next is None:
        #         # Add remaining
        #         head.next = comp
        #         break

        #     if head.next.val > comp.val:
        #         # If head list is larger, merge the comparison
        #         # list on top and swap the head
        #         tmp = head.next # remainder of chain
        #         head.next = comp
        #         comp = tmp
        #     else:
        #         ...  # just increment (no need to merge)

        #     # Increment
        #     head = head.next
        
        # # head.next = comp

        # return head