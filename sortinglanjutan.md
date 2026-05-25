# TUGAS--SORTING-BINARY-TREE-STRUKTUR-DESKRIPSI
BAGIAN 1: Sorting Lanjutan
a. Ruang & Distribusi Sort
Mengapa Radix Sort standar melanggar O(1)?
Radix Sort standar menggunakan array of 10 queues (bucket untuk digit 0–9). Setiap bucket adalah struktur dinamis yang menampung elemen secara terpisah dari array input. Total ruang yang dialokasikan adalah O(n + k), di mana n adalah jumlah elemen dan k adalah jumlah bucket. Untuk 10⁶ elemen, ini berarti alokasi memori ekstra yang signifikan — jauh melampaui batas O(1).
Bagaimana tmpArray tunggal pada Improved Merge Sort menekan overhead?
Pada Listing 12.2 & 12.4, hanya satu tmpArray berukuran n yang dialokasikan di awal, sekali saja, sebelum rekursi dimulai. Array ini dipakai ulang (reuse) di setiap pemanggilan _merge_virtual() tanpa membuat salinan baru. Tidak ada sublist fisik yang dibuat — yang ada hanya indeks virtual (left_start, mid, right_end) yang merepresentasikan batas sublist di dalam array asli. Ini berbeda dari versi berbasis slice (arr[:mid]) yang membuat array baru di setiap rekursi, menghasilkan overhead O(n log n) ruang total.
Strategi realistis jika ingin Radix Sort dengan O(1)?
Opsi paling realistis adalah American Flag Sort (in-place radix sort). Algoritmanya:
Hitung frekuensi setiap digit (counting pass) — O(k) ruang, k = 10, konstan.
Hitung prefix sum untuk menentukan posisi target setiap elemen.
Lakukan permutasi in-place dengan cycle-following.
Dampak terhadap kompleksitas waktu: tetap O(d·n) secara teori, namun konstanta praktisnya lebih besar karena pola akses memori yang tidak sekuensial (cache unfriendly). Untuk 10⁶ elemen integer, ini tetap jauh lebih cepat dari O(n log n).
