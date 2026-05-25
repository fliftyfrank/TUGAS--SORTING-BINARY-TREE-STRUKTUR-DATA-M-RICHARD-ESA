import math
from typing import List, Optional

class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class AdvancedSorter:
    def __init__(self):
        pass

    # =========================================================
    # 1. ARRAY MERGE SORT
    # =========================================================
    def sort_array(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        tmp_array = [0] * len(arr)
        self._rec_merge_sort(arr, 0, len(arr) - 1, tmp_array)
        return arr

    def _rec_merge_sort(self, arr, first, last, tmp_array):
        if first >= last:
            return
        mid = (first + last) // 2
        self._rec_merge_sort(arr, first, mid, tmp_array)
        self._rec_merge_sort(arr, mid + 1, last, tmp_array)
        self._merge_virtual(arr, first, mid, last, tmp_array)

    def _merge_virtual(self, arr, left_start, mid, right_end, tmp_array):
        a = left_start   # pointer sublist kiri
        b = mid + 1      # pointer sublist kanan
        k = left_start   # pointer tmp_array

        while a <= mid and b <= right_end:
            # Gunakan <= untuk menjamin STABILITAS
            # (elemen kiri diprioritaskan jika sama)
            if arr[a] <= arr[b]:
                tmp_array[k] = arr[a]
                a += 1
            else:
                tmp_array[k] = arr[b]
                b += 1
            k += 1

        # Salin sisa sublist kiri
        while a <= mid:
            tmp_array[k] = arr[a]
            a += 1
            k += 1

        # Salin sisa sublist kanan
        while b <= right_end:
            tmp_array[k] = arr[b]
            b += 1
            k += 1

        # Salin kembali ke arr (in-place update)
        for i in range(left_start, right_end + 1):
            arr[i] = tmp_array[i]

    # =========================================================
    # 2. LINKED LIST MERGE SORT
    # =========================================================
    def sort_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        right_head = self._split_linked_list(head)
        left_head = head
        left_sorted  = self.sort_linked_list(left_head)
        right_sorted = self.sort_linked_list(right_head)
        return self._merge_linked_lists(left_sorted, right_sorted)

    def _split_linked_list(self, head: ListNode) -> Optional[ListNode]:
        # Fast-slow pointer
        midPoint = head       # bergerak 1 langkah
        curNode  = head.next  # bergerak 2 langkah

        while curNode and curNode.next:
            midPoint = midPoint.next
            curNode  = curNode.next.next

        # Putus list di tengah
        right_head = midPoint.next
        midPoint.next = None
        return right_head

    def _merge_linked_lists(self,
                             listA: Optional[ListNode],
                             listB: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node sebagai sentinel (1 node statis)
        dummy = ListNode(0)
        tail  = dummy

        while listA and listB:
            # <= untuk menjamin STABILITAS
            if listA.data <= listB.data:
                tail.next = listA
                listA = listA.next
            else:
                tail.next = listB
                listB = listB.next
            tail = tail.next

        # Sambungkan sisa list yang belum habis
        tail.next = listA if listA else listB
        return dummy.next

    # =========================================================
    # 3. QUICK SORT dengan Median-of-Three + Depth Limiter
    # =========================================================
    def partition_quick(self, arr: List[int], first: int, last: int) -> int:
        mid = (first + last) // 2

        # --- Median-of-Three ---
        # Urutkan arr[first], arr[mid], arr[last] secara manual
        if arr[first] > arr[mid]:
            arr[first], arr[mid] = arr[mid], arr[first]
        if arr[first] > arr[last]:
            arr[first], arr[last] = arr[last], arr[first]
        if arr[mid] > arr[last]:
            arr[mid], arr[last] = arr[last], arr[mid]
        # Sekarang arr[mid] = median; tukar ke arr[first] sebagai pivot
        arr[first], arr[mid] = arr[mid], arr[first]

        pivot = arr[first]
        left  = first + 1
        right = last

        # Partisi standar (in-place)
        # Catatan: partisi ini TIDAK stable secara umum karena
        # elemen sama bisa ditukar posisinya. Untuk stability,
        # gunakan Merge Sort.
        while left <= right:
            while left <= right and arr[left] <= pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left  += 1
                right -= 1

        # Tempatkan pivot ke posisi akhirnya
        arr[first], arr[right] = arr[right], arr[first]
        return right  # posisi pivot

    def quick_sort_recursive(self, arr: List[int],
                              first: int, last: int,
                              depth: int = 0):
        if first >= last:
            return
        n = last - first + 1
        # Depth limiter: fallback ke Merge Sort jika terlalu dalam
        if n > 1 and depth > 2 * math.log2(n):
            sub = arr[first:last + 1]
            self.sort_array(sub)
            arr[first:last + 1] = sub
            return

        pivot_pos = self.partition_quick(arr, first, last)
        self.quick_sort_recursive(arr, first, pivot_pos - 1, depth + 1)
        self.quick_sort_recursive(arr, pivot_pos + 1, last, depth + 1)
