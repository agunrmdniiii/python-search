# python-search
Hari ini saya belajar sequential search dan binary search. Sequential search adalah metode pencarian linear dengan memeriksa setiap elemen satu per satu. Binary search adalah metode pencarian efisien untuk daftar terurut, dengan membagi daftar menjadi setengah bagian pada setiap langkahnya. Sequential search cocok untuk daftar tidak terurut, sedangkan binary search cocok untuk daftar terurut.

Cara percobaan 10: 
1. Pertama, daftar `my_list` didefinisikan dengan nilai `[6, 7, 8, 9, 1, 2, 3, 4, 5]`. Daftar ini mewakili urutan yang telah dirotasi dari urutan aslinya.

2. Fungsi `binary_search_rotation` didefinisikan dengan satu parameter, yaitu `data`. Pada awalnya, nilai `low` diatur sebagai 6, yang merupakan indeks pertama setelah elemen terakhir dalam daftar. Nilai `high` diatur sebagai `len(data) - 1`, yaitu indeks terakhir dalam daftar.

3. Selama `low` lebih kecil dari `high`, dilakukan perulangan untuk mencari indeks rotasi terkecil.

4. Pada setiap iterasi, indeks tengah `mid` dihitung dengan mengambil nilai tengah dari `low` dan `high` menggunakan operasi pembagian bulat `//`.

5. Kemudian, dilakukan pengecekan apakah `data[mid]` lebih besar dari `data[high]`. Jika benar, artinya rotasi terjadi pada bagian kanan indeks `mid`. Dalam hal ini, `low` diubah menjadi `mid + 1` untuk memperbarui batas bawah pencarian.

6. Jika `data[mid]` tidak lebih besar dari `data[high]`, artinya rotasi terjadi pada bagian kiri atau pada indeks `mid` atau sebelumnya. Dalam hal ini, `high` diubah menjadi `mid` untuk memperbarui batas atas pencarian.

7. Langkah-langkah 4-6 diulang hingga `low` tidak lagi lebih kecil dari `high`, sehingga ditemukan indeks rotasi terkecil.

8. Setelah perulangan selesai, nilai `low` akan menjadi indeks rotasi terkecil dalam daftar, dan nilainya dikembalikan menggunakan pernyataan `return low`.

9. Pada baris selanjutnya, fungsi `binary_search_rotation` dipanggil dengan argumen `my_list`, dan hasilnya disimpan dalam variabel `rotation_index`.

10. Terakhir, menggunakan pernyataan `print`, nilai `rotation_index` dicetak untuk memberikan output berupa teks yang menyatakan indeks rotasi terkecil dalam daftar.

Jadi, dalam kasus ini, output yang diharapkan akan menjadi:

```
Indeks rotasi terkecil adalah 4
```

Ini berarti indeks rotasi terkecil dalam daftar `[6, 7, 8, 9, 1, 2, 3, 4, 5]` adalah 4.

Cara Percobaan 11 :
1. Pertama, inisialisasi variabel `max_count` dan `most_frequent` dengan nilai 0 dan None, masing-masing untuk melacak jumlah kemunculan maksimum dan elemen yang paling sering muncul.
2. Tentukan rentang pencarian awal dari indeks pertama hingga indeks terakhir dalam daftar.
3. Dalam loop while, lakukan pencarian selama rentang pencarian tidak kosong.
4. Hitung indeks tengah `mid` dalam rentang pencarian dan inisialisasi `count` sebagai 1.
5. Cari elemen yang sama dengan elemen di `mid` di sebelah kiri dan sebelah kanan menggunakan dua loop while terpisah.
6. Jika ditemukan elemen yang sama, tambahkan `count` dan perbarui indeks `left` dan `right` sesuai dengan pencarian yang dilakukan.
7. Setelah selesai mencari di kedua sisi, bandingkan `count` dengan `max_count`. Jika `count` lebih besar, perbarui `max_count` dan `most_frequent` dengan elemen di `mid`.
8. Jika `count` adalah 1, artinya elemen yang sedang diperiksa adalah elemen unik, maka hentikan pencarian.
9. Perbarui rentang pencarian dengan mengatur `low` atau `high` sesuai dengan hasil pencarian sebelumnya.
10. Ulangi langkah 3-9 hingga rentang pencarian menjadi kosong.
11. Kembalikan elemen `most_frequent` sebagai hasil.
12. Buat daftar `my_list` dengan beberapa elemen yang diuji.
13. Panggil fungsi `binary_search_most_frequent` dengan daftar `my_list` dan simpan hasilnya di `most_frequent_element`.
14. Cetak hasilnya dengan memformat teks yang sesuai.

Hasil yang diharapkan:
Elemen yang paling sering muncul adalah 8

Cara Percobaan 12 :


1. saya memiliki daftar `names` yang berisi beberapa nama yang diurutkan: 'Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', dan 'George'.
2. Kemudian, saya meminta pengguna untuk memasukkan nama yang ingin dicari melalui input.
   - Misalkan pengguna memasukkan "Emma" sebagai nama yang dicari.
3. Selanjutnya, saya memanggil fungsi `binary_search` dengan argumen `names` (daftar nama) dan `target_name` (nama yang ingin dicari).
   - Pada saat ini, `low` diinisialisasi dengan 6 dan `high` diinisialisasi dengan 6 (panjang daftar dikurangi 1).
4. Algoritma binary search dimulai dalam loop while. Di setiap iterasi:
   - saya menghitung nilai tengah `mid` dengan menggunakan rumus `(low + high) // 2`, yang akan menjadi indeks elemen tengah dalam rentang pencarian.
   - saya membandingkan elemen di `mid` (yaitu 'Frank') dengan `target_name` ('Emma').
     - Karena elemen di `mid` bukan 'Emma', maka saya melanjutkan ke langkah berikutnya.
   - Karena 'Frank' ('names[mid]') kurang dari 'Emma' (`target_name`), saya perbarui `low` menjadi `mid + 1`, sehingga `low` sekarang bernilai 7.
5. saya kembali ke awal loop while dan melakukan iterasi berikutnya.
   - Kali ini, `low` adalah 7 dan `high` tetap 6.
   - saya menghitung `mid` sebagai `(low + high) // 2` yang menghasilkan 6 (indeks elemen 'George').
   - saya membandingkan elemen di `mid` ('George') dengan `target_name` ('Emma').
     - Karena elemen di `mid` bukan 'Emma', maka saya melanjutkan ke langkah berikutnya.
   - Karena 'George' ('names[mid]') lebih besar dari 'Emma' (`target_name`), saya perbarui `high` menjadi `mid - 1`, sehingga `high` sekarang bernilai 5.
6. saya kembali ke awal loop while dan melakukan iterasi berikutnya.
   - Kali ini, `low` tetap 7 dan `high` adalah 5.
   - Karena `low` lebih besar dari `high`, kondisi while menjadi salah dan loop while berakhir.
7. Karena tidak ada iterasi dalam loop while yang menemukan 'Emma', maka saya keluar dari loop dan mengembalikan -1 sebagai hasil pencarian.
8. Setelah itu, saya memeriksa hasil pencarian. Jika `index` tidak sama dengan -1, artinya nama ditemukan, maka saya mencetak "Nama ditemukan pada indeks" diikuti dengan nilai `index`.
   - Dalam contoh ini, karena `index` sama dengan -1, pesan "Nama tidak ditemukan" dicetak.

Hasil yang diharapkan:
```
Nama tidak ditemukan
