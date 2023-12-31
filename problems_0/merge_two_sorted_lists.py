def mergeTwoLists(list1, list2):
    beg = cur = ListNode(0)
    while list1 and list2:
        if list1.val > list2.val:
            cur.next = list2
            list2 = list2.next
        else:
            cur.next = list1
            list1 = list1.next
        cur = cur.next
    cur.next = list1 or list2
    return beg.next


