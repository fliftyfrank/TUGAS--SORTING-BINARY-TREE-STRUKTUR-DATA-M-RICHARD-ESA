Batas Teoretis & Decision Tree
Mengapa heapsort tidak melanggar Ω(n log n)?
Heapsort adalah comparison-based sort — ia hanya menggunakan operasi arr[i] > arr[j] untuk membuat keputusan. Dengan demikian lower bound Ω(n log n) tetap berlaku. Heapsort mencapai tepat O(n log n) dalam semua kasus (best, average, worst), sehingga ia memenuhi batas bawah tersebut, bukan melanggarnya.
Bagaimana null link mendeteksi token tidak valid di decision tree Morse Code?
Setiap node pohon Morse merepresentasikan satu karakter. Anak kiri = . (dot), anak kiri = - (dash). Jika setelah memproses seluruh token, pointer berakhir di None (null link) — berarti tidak ada karakter yang terdaftar untuk urutan sinyal tersebut → token tidak valid.
Mengapa rekursif lebih cocok dari iteratif untuk membangun decision tree?
Struktur pohon secara alami bersifat rekursif: setiap subtree adalah pohon lagi dengan struktur identik. Fungsi rekursif langsung merepresentasikan definisi ini — buildTree(node, tokens) memanggil dirinya untuk anak kiri dan kanan. Versi iteratif memerlukan stack eksplisit yang mengelola state traversal secara manual, membuat kode lebih kompleks dan sulit dibaca tanpa keuntungan asimptotik.
