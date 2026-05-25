Ketika curNode mencapai akhir list, midPoint tepat berada di tengah. Ini karena rasio kecepatan 2:1 — saat pointer cepat menempuh n langkah, pointer lambat baru menempuh n/2 langkah. Tidak perlu menghitung panjang terlebih dahulu.
Mengapa dummy node + tail reference tidak butuh alokasi memori tambahan?
Operasi ini hanya memodifikasi pointer .next dari node-node yang sudah ada. Tidak ada ListNode baru yang dibuat. Node-node dari listA dan listB langsung "dirangkai ulang" tanpa biaya alokasi.
Kompleksitas ruang O(log n) berasal semata dari call stack rekursi — setiap level rekursi menyimpan frame kecil (beberapa pointer lokal), dan kedalaman rekursi maksimum adalah log₂(n) karena list selalu dibagi dua.
