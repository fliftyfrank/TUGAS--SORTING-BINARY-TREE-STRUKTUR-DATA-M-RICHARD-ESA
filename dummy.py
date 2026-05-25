dummy = ListNode(0)  # 1 node statis, tidak ikut list
tail  = dummy

# Selama merge:
tail.next = listA   # hanya mengubah pointer, bukan alokasi
tail = tail.next
