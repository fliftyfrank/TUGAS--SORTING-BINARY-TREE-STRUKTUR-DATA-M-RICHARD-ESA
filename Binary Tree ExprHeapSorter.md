Pohon Ekspresi & Traversal
Langkah-demi-langkah _buildTree() untuk ((8 * 5) + (9 / (7 - 4))):
Token antrian (deque): ( ( 8 * 5 ) + ( 9 / ( 7 - 4 ) ) )
Langkah
Token Dibaca
Aksi
1
(
Buat node baru, rekursi ke kiri
2
(
Buat node baru, rekursi ke kiri
3
8
Return node operand {val:8}
4
*
Simpan operator di node saat ini
5
5
Return node operand {val:5}
6
)
Selesai subtree (8*5)
7
+
Simpan operator di root
8
(
Buat node baru, rekursi ke kiri
9
9
Return node operand {val:9}
10
/
Simpan operator
11
(
Rekursi lagi
12
7
Return {val:7}
13
-
Simpan operator
14
4
Return {val:4}
15
)
Selesai (7-4)
16
)
Selesai (9/(7-4))
17
)
Selesai root

kode:
+
       / \
      *    /
     / \  / \
    8   5 9   -
             / \
            7   4
            Mengapa postorder otomatis menghasilkan postfix valid?
Postorder mengunjungi: kiri → kanan → root. Untuk node operator, ini berarti kedua operand selalu dicetak sebelum operatornya — persis definisi notasi postfix. Tidak ada ambiguitas precedence karena struktur pohon sudah merepresentasikan precedence secara implisit melalui kedalaman node.
Inorder (kiri → root → kanan) menghasilkan notasi infix, tetapi karena pohon ekspresi bisa memiliki kedalaman asimetris, tanda kurung harus ditambahkan secara eksplisit untuk menjamin urutan evaluasi yang benar (seperti pada Listing 13.7).
Kedalaman stack rekursi _buildString() untuk pohon tinggi h:
Setiap pemanggilan rekursif turun satu level. Untuk pohon dengan tinggi h, maksimum h+1 frame aktif di stack secara bersamaan → kedalaman stack rekursi = O(h).
