def removeElements(head):
    cur = prev = ListNode(-1, head)
    while head:
        if head.val == val:
            prev.next = head.next
            head = head.next
            continue
        prev, head = prev.next, head.next
    return cur.next

