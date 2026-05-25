Batas Teoretis & Paradigma Sorting
Mengapa Radix Sort O(dn) tidak kontradiktif dengan lower bound Ω(n log n)?
Lower bound Ω(n log n) hanya berlaku untuk comparison-based sort — algoritma yang satu-satunya cara mendapatkan informasi tentang urutan elemen adalah melalui operasi perbandingan a < b. Buktinya via decision tree: tree harus memiliki minimal n! daun, sehingga tinggi minimal adalah log₂(n!) = Ω(n log n).
Radix Sort tidak melakukan perbandingan antar elemen. Ia mengekstrak digit dan mendistribusikan elemen ke bucket berdasarkan nilai digit tersebut — bukan hasil perbandingan relatif. Karena model komputasinya berbeda, lower bound comparison sort tidak berlaku.
Dua asumsi implisit yang membuat Radix Sort "melampaui" batas:
Kunci memiliki digit/representasi dengan panjang d yang konstan atau kecil. Jika d = O(log n), maka O(dn) = O(n log n) — tidak lebih cepat. Radix Sort benar-benar linear hanya jika d = O(1), yaitu kunci memiliki panjang tetap yang tidak bergantung pada n.
Range nilai kunci k harus terbatas (bounded). Setiap digit harus berasal dari alphabet berukuran k yang konstan (misal 0–9, atau 0–255). Jika k sangat besar (misal kunci adalah string arbitrary), ukuran bucket meledak dan kompleksitas ruang serta waktu tidak lagi O(n).
Dengan kata lain: Radix Sort "curang" bukan karena lebih pintar, tapi karena ia mengeksploitasi struktur internal kunci yang tidak dimanfaatkan oleh comparison sort.
