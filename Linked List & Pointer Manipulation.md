Linked List & Pointer Manipulation
Bagaimana _splitLinkedList() menemukan titik tengah dalam satu traversal?
Teknik ini disebut fast-slow pointer (Floyd's tortoise and hare):
midPoint = head        # bergerak 1 langkah
curNode  = head.next   # bergerak 2 langkah

while curNode and curNode.next:
    midPoint = midPoint.next
    curNode  = curNode.next.next
