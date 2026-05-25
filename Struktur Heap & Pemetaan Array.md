Struktur Heap & Pemetaan Array
Mengapa rumus indeks hanya valid untuk complete binary tree?
Rumus parent = (i-1)//2, left = 2i+1, right = 2i+2 mengasumsikan bahwa setiap level terisi penuh dari kiri ke kanan tanpa "lubang". Jika ada node yang hilang di tengah (bukan complete), mapping indeks array ke posisi tree menjadi salah — node yang seharusnya di posisi i secara logis bisa berada di indeks berbeda.
Bagaimana sift_down() memulihkan heap order setelah ekstraksi akar?
Pindahkan elemen terakhir ke posisi root (indeks 0).
Bandingkan root dengan kedua anaknya.
Tukar root dengan anak terbesar jika anak > root.
Ulangi dari posisi anak yang baru ditempati, terus ke bawah.
Berhenti jika node lebih besar dari kedua anak, atau sudah daun.
Jumlah perbandingan maksimum dalam satu sift-down untuk heap ukuran n:
Tinggi heap = ⌊log₂(n)⌋
Setiap level: 2 perbandingan (bandingkan kiri vs kanan, lalu bandingkan terbesar vs parent)
Total maksimum: 2·⌊log₂(n)⌋ perbandingan = O(log n)
