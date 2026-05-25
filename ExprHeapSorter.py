from typing import List, Optional
from collections import deque

class ExprHeapSorter:
    def __init__(self, expr_str: str):
        # Hilangkan spasi agar tokenisasi lebih mudah
        self.expr = expr_str.replace(" ", "")
        self.values = []

    # =========================================================
    # 1. EXPRESSION TREE
    # =========================================================
    def parse_and_evaluate(self) -> List[int]:
        tokens = deque(self.expr)
        root = self._build_tree(tokens)
        result = self._eval_tree(root)
        self.values = [result]
        return self.values

    def _build_tree(self, tokens: deque) -> Optional[dict]:
        if not tokens:
            return None

        token = tokens.popleft()

        if token == '(':
            # Bangun subtree kiri
            left  = self._build_tree(tokens)
            # Token berikutnya adalah operator
            op    = tokens.popleft()
            # Bangun subtree kanan
            right = self._build_tree(tokens)
            # Konsumsi ')'
            if tokens and tokens[0] == ')':
                tokens.popleft()
            return {'val': op, 'left': left, 'right': right}

        elif token == ')':
            # Seharusnya tidak terjadi jika ekspresi valid
            return None

        else:
            # Operand: kumpulkan digit multi-karakter
            num_str = token
            while tokens and tokens[0].isdigit():
                num_str += tokens.popleft()
            return {'val': int(num_str), 'left': None, 'right': None}

    def _eval_tree(self, node: Optional[dict]):
        if node is None:
            raise ValueError("Node kosong saat evaluasi")

        # Daun = operand
        if node['left'] is None and node['right'] is None:
            return node['val']

        # Evaluasi postorder
        left_val  = self._eval_tree(node['left'])
        right_val = self._eval_tree(node['right'])
        op = node['val']

        if op == '+': return left_val + right_val
        if op == '-': return left_val - right_val
        if op == '*': return left_val * right_val
        if op == '/':
            if right_val == 0:
                raise ValueError("Division by zero")
            return left_val // right_val  # integer division
        raise ValueError(f"Operator tidak valid: {op}")

    # =========================================================
    # 2 & 3. HEAP + HEAPSORT IN-PLACE
    # =========================================================
    def heapsort_inplace(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n <= 1:
            return arr

        # Fase 1: Build max-heap dari bawah ke atas
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(arr, n, i)

        # Fase 2: Ekstraksi berulang
        for end in range(n - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]  # swap root ke akhir
            self._sift_down(arr, end, 0)           # pulihkan heap

        return arr

    def _sift_down(self, arr: List[int], heap_size: int, idx: int):
        while True:
            largest = idx
            left    = 2 * idx + 1
            right   = 2 * idx + 2

            if left < heap_size and arr[left] > arr[largest]:
                largest = left
            if right < heap_size and arr[right] > arr[largest]:
                largest = right

            if largest == idx:
                break  # Heap order terpenuhi

            arr[idx], arr[largest] = arr[largest], arr[idx]
            idx = largest  # lanjut sift-down ke bawah

    # =========================================================
    # 4. COMPLETE TREE VALIDATOR
    # =========================================================
    def is_complete_tree(self, arr: List[int]) -> bool:
        n = len(arr)
        if n == 0:
            return True

        # Pada complete binary tree yang dipetakan ke array 0..n-1,
        # semua indeks 0 sampai n-1 harus terisi tanpa lubang.
        # Cukup verifikasi: untuk setiap node i yang memiliki anak,
        # anak tersebut harus berada di indeks < n.
        found_missing = False
        for i in range(n):
            left  = 2 * i + 1
            right = 2 * i + 2

            if left < n:
                if found_missing:
                    # Ada node setelah "lubang" → tidak complete
                    return False
            else:
                # Node ini tidak punya anak kiri → mulai zona "daun"
                found_missing = True
                continue

            if right < n:
                if found_missing:
                    return False
            else:
                found_missing = True

        return True


# =========================================================
# DEMO & PENGUJIAN
# =========================================================
if __name__ == "__main__":
    print("=" * 50)
    print("TEST AdvancedSorter")
    print("=" * 50)

    sorter = AdvancedSorter()

    # Test Array Merge Sort
    arr = [5, 3, 8, 1, 9, 2, 7, 4, 6]
    print("Array asli   :", arr)
    print("Array terurut:", sorter.sort_array(arr))

    # Test Linked List Sort
    nodes = [ListNode(x) for x in [5, 3, 8, 1, 9, 2]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = sorter.sort_linked_list(nodes[0])
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print("Linked list terurut:", result)

    # Test Quick Sort
    arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]  # worst-case descending
    print("Sebelum QS   :", arr2)
    sorter.quick_sort_recursive(arr2, 0, len(arr2) - 1)
    print("Sesudah QS   :", arr2)

    print("\n" + "=" * 50)
    print("TEST ExprHeapSorter")
    print("=" * 50)

    expr = "((8*5)+(9/(7-4)))"
    ehs = ExprHeapSorter(expr)
    val = ehs.parse_and_evaluate()
    print(f"Ekspresi: {expr}")
    print(f"Hasil evaluasi: {val[0]}")  # 8*5=40, 7-4=3, 9/3=3, 40+3=43

    data = [40, 3, 15, 7, 22, 8, 1, 43]
    print("Data asli     :", data)
    ehs2 = ExprHeapSorter("")
    sorted_data = ehs2.heapsort_inplace(data[:])
    print("Heapsort hasil:", sorted_data)
    print("Complete tree? :", ehs2.is_complete_tree(sorted_data))
