def isPalindrome(head):
    left  = right = head
    while right.next and right.next.next:
        left = left.next
        right = right.next.next
    if right.next: left = left.next
    
    prev = None
    while left:
        nxt = left.next
        left.next = prev
        prev = left
        left = nxt
    
    while head and prev:
        if head.val != prev.val:
            return False
        head, prev = head.next, left.next
    return True
        
