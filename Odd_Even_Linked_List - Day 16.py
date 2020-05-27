# if not head:return None
        # even=head.next
        # i=head
        # j=even
        # while i.next and j.next:
        #     print(i.val,i.next.val,j.val,j.next.val)
        #     i.next=j.next
        #     i=i.next
        #     j.next=i.next
        #     j=j.next
        # i.next=even
        # return head
    
        even=ListNode(0)
        odd=ListNode(0)
        evenHead,oddHead=even,odd
        t=1
        while head:
            if t%2==1:
                odd.next=head
                odd=odd.next
            else:
                even.next=head
                even=even.next
            t+=1
            head=head.next
        even.next=None
        odd.next=evenHead.next
        return oddHead.next