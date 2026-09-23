#  POSTTEST 1 - Class, Atribut, Method, Getter & Setter
🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️

> Program ini dirancang untuk mensimulasikan sistem operasional **Optik Cahaya**. Sistem mengelola inventaris produk kacamata (frame, lensa, dan aksesori), pencatatan stok cabang, serta eksekusi transaksi penjualan lengkap dengan penambahan bonus otomatis untuk pembelian kacamata.

<details>
<summary><h2> Identitas Praktikan</h2></summary>

* **Nama** : Nur Azizah Islamiyah
* **NIM** : 2509106018
* **Kelas** : A1 2025
* **Mata Kuliah** : Praktikum Pemrograman Berbasis Objek
* **Tema** : Sistem Manajemen Optik Cahaya

</details>
<details>
<summary><h2> Struktur Class & Enkapsulasi</h2></summary>

Sistem ini menggunakan tiga class utama yang saling berinteraksi:

### 1. `ProdukOptik`
Bertanggung jawab atas entitas produk (seperti Frame, Lensa, dan Aksesoris).
* **Atribut Class:**
  * `nama_optik`: Nama toko (`'Optik Cahaya'`).
  * `produk_terdaftar`: Penghitung otomatis jumlah objek produk yang telah diinstansiasi.
* **Atribut Instance:**
  * `id_sku`: Kode unik barang.
  * `nama_produk`: Nama lengkap produk.
  * `kategori`: Kategori produk (`FRM`, `LNS`, atau `AKS`).
  * `__harga`: Harga produk *(Private)*.
  * `__stok`: Kuantitas produk yang tersedia *(Private)*.
* **Getter & Setter (Enkapsulasi):**
  * `harga`: Getter untuk membaca `__harga`, Setter memvalidasi agar harga tidak boleh $\le 0$.
  * `stok`: Getter untuk membaca `__stok`, Setter memvalidasi agar stok tidak boleh negatif.
* **Instance Method:**
  * `kurangi_stok(jumlah)`: Mengurangi kuantitas produk jika stok mencukupi dan menampilkan pesan peringatan jika stok kurang.
  * `tampil_detail()`: Menampilkan informasi produk (SKU, Nama, Kategori, Harga, Stok) dalam format tabel.
* **Class Method (`buat_sku`):**
  * Memebuat kode SKU dengan format `[KAT]-[MERK]-[FITUR]-[UKURAN]`.
* **Static Method (`hitung_omset`):**
  * Menghitung potensi omset dari suatu produk berdasarkan perkalian harga dan stok.

---

### 2. `Inventory`
Mengelola distribusi dan ketersediaan stok produk pada cabang-cabang optik.
* **Atribut Class:**
  * `max_gudang`: Kapasitas maksimal penyimpanan gudang pusat (default: `1000`).
* **Atribut Instance:**
  * `nama_cabang`: Nama lokasi cabang optik.
  * `daftar_barang`: List penampung objek `ProdukOptik` yang terdaftar di cabang tersebut.
  * `__pin_akses`: PIN privat untuk keamanan pengubahan data cabang *(Private)*.
* **Getter & Setter (Enkapsulasi):**
  * `pin_akses`: Getter mengembalikan nilai PIN, Setter memvalidasi bahwa PIN harus tepat 3 digit angka.
* **Instance Method:**
  * `tambah_produk(produk)`: Memasukkan objek produk ke dalam list `daftar_barang` milik cabang.
  * `tampil_stok()`: Menampilkan seluruh daftar produk beserta detailnya pada cabang terkait.
* **Class Method (`update_kapasitas_gdg`):**
  * Memperbarui batas kapasitas maksimal gudang pusat (`max_gudang`) untuk seluruh sistem.

---

### 3. `Transaksi`
Menangani pencatatan transaksi pembelian, pengalkulasian total, serta pencetakan nota pelanggan.
* **Atribut Class:**
  * `transaksi_selesai`: Penghitung jumlah transaksi yang berhasil diproses.
  * `bonus`: List bonus otomatis untuk pembelian kacamata (`'Kotak Kacamata Hardcase Optik Cahaya'` dan `'Lap Kain Microfiber Premium'`).
* **Atribut Instance:**
  * `id_transaksi`: Kode transaksi unik.
  * `nama_pelanggan`: Nama pelanggan yang bertransaksi.
  * `item_pembelian`: List dictionary penampung barang, jumlah (*qty*), dan subtotal.
  * `status_pembayaran`: Status transaksi (default: `'Pending'`).
  * `__total_bayar`: Akumulasi nilai belanjaan pelanggan *(Private)*.
* **Getter & Setter (Enkapsulasi):**
  * `total_bayar`: Getter membaca `__total_bayar`, Setter mencegah nilai total bernilai negatif.
* **Instance Method:**
  * `tambah_item_pembelian(produk, qty=1)`: Mengurangi stok barang secara langsung di inventaris, mengalkulasi subtotal, dan menambahkan ke daftar belanjaan.
  * `cetak_nota()`: Mencetak nota penjualan, mengecek kelayakan bonus kacamata (`FRM`/`LNS`), serta mengupdate penghitung `transaksi_selesai`.

> Otomatis memberikan bonus berupa *Kotak Kacamata Hardcase* dan *Lap Kain Microfiber Premium* jika pelanggan membeli produk kategori Frame (`FRM`) atau Lensa (`LNS`).

</details>
<details>
<summary><h2> Panduan Pengujian Program</h2></summary>

Alur pengujian di dalam fungsi `if __name__ == '__main__':` menjalankan beberapa skenario untuk membuktikan bahwa sistem berjalan dengan baik:

### 1. Pembuatan Objek
* Sistem membuat 3 produk awal dengan metode berbeda (inisialisasi langsung dan melalui `buat_sku`).
* Produk didaftarkan ke cabang **Optik Cahaya Samarinda Central Plaza** dan **Optik Cahaya Bontang City Mall**.
* Membuat 2 riwayat transaksi yang sudah berhasil 

### 2. Pemanggilan Method
* `stok_cab1.tambah_produk(produk1)` menambahkan produk ke inventory gudang cabang **Optik Cahaya Samarinda Central Plaza**, `stok_cab1.tampil_stok()` menampilkan daftar stok awal cabang dalam bentuk tabel di terminal.
* Memanggil `ProdukOptik.hitung_omset()` untuk menampilkan total nilai barang dari salah satu produk.
* Memperbarui batas maksimal kapasitas penyimpanan seluruh jaringan retail melalui class method `Inventory.update_kapasitas_gdg()`.
* `transaksi1.tambah_item_pembelian()` menambahkan item ke transaksi, lalu `transaksi1.cetak_nota` akan membuat dan menampilkan detail pembelian dari transaksi 1. 
* Melihat stok produk yang berkurang setelah transaksi selesai `stok.cab1_tampil_stok()`.

### 3. Pengujian Validasi
Program sengaja menguji batasan aturan enkapsulasi untuk memastikan sistem tidak rusak oleh input ilegal:
* **Validasi Stok & Harga:** Mencoba mengubah stok menjadi negatif (`-2`) dan harga menjadi negatif (`-50000`). Sistem akan menolak perubahan dan menampilkan pesan peringatan.
* **Validasi PIN Akses:** Memasukkan PIN berupa huruf (`ABC`). Sistem akan menolaknya karena PIN wajib berupa 3 digit angka.
* **Validasi Transaksi:** Memasukkan nilai total bayar negatif. Sistem otomatis memblokir nilai tersebut.

### 4. Alur Simulasi Transaksi Pelanggan
* Pelanggan bernama **Nur Azizah** (`TRX-1001`) melakukan pembelian beberapa item sekaligus.
* Saat item ditambahkan, sistem memotong stok asli produk di inventaris cabang.
* Sistem mencetak nota resmi. Karena terdapat pembelian produk kategori `FRM` dan `LNS`, teks **`[FREE BONUS]`** otomatis muncul di lembar nota.
* Menampilkan ulang daftar stok cabang untuk memastikan kuantitas barang pasca-transaksi sudah berkurang dengan benar.