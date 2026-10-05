# Pertemuan 06 — Nested Loop, Pola, Akumulasi, dan Pencacahan

## Identitas
- Nama: Siti Nurjanah
- NIM: 2225250110
- Kelas: 3E

## Tujuan
Menerapkan nested loop untuk membuat pola dan memproses pasangan data, serta menggunakan akumulasi dan pencacahan dalam program Python.

## Struktur Folder

```text
pertemuan-06-nested-loop-2225250110/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_pasangan_indeks.py
│   ├── 02_pola_segitiga.py
│   ├── 03_jumlah_per_baris.py
│   └── 04_hitung_pasangan.py
└── tugas/
    └── tabel_perkalian_dan_statistik.py
```

## Cara Menjalankan

Jalankan program melalui terminal VS Code dengan perintah:

```text
python latihan/01_pasangan_indeks.py
python latihan/02_pola_segitiga.py
python latihan/03_jumlah_per_baris.py
python latihan/04_hitung_pasangan.py
python tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas

1. Memasukkan bilangan bulat positif `n`.
2. Memvalidasi agar `n` lebih besar dari 0.
3. Menyiapkan `total_semua` dan `count_genap`.
4. Menggunakan nested loop dengan `i` dan `j` dari 1 sampai `n`.
5. Menghitung `hasil = i * j`.
6. Menambahkan hasil ke jumlah baris dan total keseluruhan.
7. Menghitung banyak hasil perkalian yang genap.
8. Menampilkan jumlah setiap baris.
9. Menampilkan total semua hasil dan jumlah hasil genap.

## Pengujian

| Input n | Total Semua Hasil | Jumlah Hasil Genap |
|---|---:|---:|
| 1 | 1 | 0 |
| 2 | 9 | 3 |
| 3 | 36 | 5 |

Semua test case berhasil dijalankan.

## Analisis Efisiensi

Program menggunakan dua buah perulangan bersarang. Jika nilai `n` bertambah, jumlah proses perkalian bertambah sekitar `n × n`, sehingga kompleksitas waktunya adalah O(n²).

## Refleksi

Melalui latihan dan tugas ini, saya memahami penggunaan nested loop untuk memproses pasangan nilai, membuat pola, melakukan akumulasi, dan melakukan pencacahan. Saya juga belajar melakukan pengujian program menggunakan beberapa nilai input.