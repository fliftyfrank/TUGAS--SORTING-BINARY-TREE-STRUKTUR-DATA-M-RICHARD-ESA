Quick Sort Worst-Case & Pivot Strategy
Mengapa data descending menyebabkan O(n²)?
Pada partitionSeq() standar dengan pivot = elemen pertama:
Array descending: [n, n-1, n-2, ..., 2, 1]
Pivot selalu elemen terbesar di subarray tersisa
Pointer left langsung melewati pivot, right tidak bergerak jauh
Hasil partisi: subarray kiri berukuran 0, subarray kanan berukuran n-1
Ini menghasilkan rekursi dengan kedalaman n (bukan log n), dan setiap level melakukan O(n) perbandingan → total O(n²).
Pada data descending, median-of-three selalu memilih nilai tengah yang membelah array lebih seimbang → kedalaman rekursi turun mendekati O(log n) → waktu O(n log n).
Kelayakan pada singly linked list:
Median-of-three tidak efisien pada singly linked list karena:
Mengakses elemen ke-mid membutuhkan traversal O(n)
Mengakses elemen ke-last juga O(n)
Biaya tambahan ini muncul di setiap level rekursi
Solusi yang lebih cocok untuk linked list adalah tetap menggunakan Merge Sort (seperti Modul B), yang secara natural O(n log n) tanpa masalah pivot. Jika Quick Sort tetap diinginkan, pilih pivot = head node saja dan tambahkan depth limiter (fallback ke Merge Sort jika kedalaman > 2·log₂(n)).
