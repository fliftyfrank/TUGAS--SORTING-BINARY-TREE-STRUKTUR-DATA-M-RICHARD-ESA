Heapsort In-Place vs Simple
Aspek
Simple Heapsort
In-Place Heapsort
Ruang tambahan
O(n) — butuh array terpisah untuk hasil
O(1) — hanya variabel indeks
Pola akses memori
Lebih cache-friendly saat ekstraksi (akses sekuensial ke array output)
Kurang cache-friendly — swap root ke akhir menyebabkan akses melompat-lompat
Risiko overflow RAM
Tinggi — untuk n=10⁶ integer (4 byte), butuh ~4 MB ekstra
Minimal — hanya beberapa variabel integer
Mengapa in-place heapsort tetap O(n log n)?
Fase build-heap: O(n) — dapat dibuktikan dengan analisis amortized (jumlah total perbandingan di semua sift-down dari bawah ke atas = O(n))
Fase ekstraksi: n-1 kali ekstraksi, masing-masing sift-down O(log n) → total O(n log n)
Swap yang terjadi di setiap ekstraksi hanya O(1) per operasi, tidak mengubah analisis asimptotik
