# POSTTEST 2 - Relasi UML & Inheritance
🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ ─── 🕶️ 

> Program ini merupakan pengembangan dari **Sistem Manajemen Optik Cahaya** berbasis Python dengan menerapkan konsep **Inheritance (Pewarisan)**, **Method Overriding**, **Encapsulation (Getter & Setter)**, serta **Relasi Antar Kelas (Agregasi, Komposisi, dan Asosiasi)** sesuai dengan prinsip Pemrograman Berorientasi Objek (PBO).

<details>
<summary><h2> Identitas Praktikan</h2></summary>

* **Nama** : Nur Azizah Islamiyah
* **NIM** : 2509106018
* **Kelas** : A1 2025
* **Mata Kuliah** : Praktikum Pemrograman Berbasis Objek
* **Tema** : Sistem Manajemen Optik Cahaya

</details>

<details>
<summary><h2> Struktur Program</h2></summary>

```text
POSTTEST_PBO/
├── posttest-2/
│   └── posttest-2.py        # File Kode Utama 
│   └── readme.md            # Laporan Program
```

</details>

<details>
<summary><h2> Struktur Class & Enkapsulasi</h2></summary>

### 1. Penerapan Konsep PBO

* **Inheritance (Pewarisan):**
  Class `ProdukOptik` bertindak sebagai Superclass yang mewariskan atribut dasar (`id_sku`, `nama_produk`, `kategori`, `_harga`, `_stok`) dan method utama ke Subclass khusus: `Frame`, `Lensa`, dan `Aksesoris`.

* **Method Overriding:**
  Method `tampil_detail()` di-override pada tiap subclass (`Frame`, `Lensa`, `Aksesoris`). Masing-masing subclass memanggil `super().tampil_detail()` untuk menampilkan informasi dasar, lalu menambahkan kolom spesifikasi unik produk pada bagian kanan tabel.

* **Encapsulation & Protection:**
  Atribut disembunyikan menggunakan konvensi protected (`_harga`, `_stok`) dan private (`__pin_akses`, `__total_bayar`), kemudian diakses secara aman melalui `@property` dan `@setter` dengan aturan validasi:
  * Harga harus $> 0$.
  * Stok tidak boleh negatif.
  * PIN Akses wajib berupa 3 digit angka.
  * Total bayar transaksi tidak boleh negatif.

* **Relasi Antar Kelas (UML Alignment):**
  * **Agregasi (`Inventory` $\rightarrow$ `ProdukOptik`):** Class `Inventory` menyimpan daftar objek `ProdukOptik` di dalam list `daftar_barang`. Objek produk dibuat secara independen di luar instance `Inventory`.
  * **Komposisi (`Transaksi` $\rightarrow$ `item_pembelian`):** Keranjang belanja beserta kalkulasi subtotal dikelola penuh di dalam instance `Transaksi`.
  * **Asosiasi (`Transaksi` $\leftrightarrow$ `ProdukOptik`):** Method `tambah_item_pembelian()` memanggil method `kurangi_stok()` pada objek `ProdukOptik` untuk memotong stok secara otomatis.

---

### 2. Rincian Class & Subclass

#### A. Superclass: `ProdukOptik`
* **Atribut Class:** `nama_optik` (`'Optik Cahaya'`), `produk_terdaftar`.
* **Atribut Instance:** `id_sku`, `nama_produk`, `kategori`, `_harga` *(Protected)*, `_stok` *(Protected)*.
* **Method:**
  * `harga` & `stok` (Getter & Setter dengan validasi).
  * `tampil_detail()`: Menampilkan format dasar data produk.
  * `kurangi_stok(jumlah)`: Memotong stok jika kuantitas mencukupi.
  * `hitung_omset(harga, stok)` *(Static Method)*: Menghitung estimasi nilai omset produk.

#### B. Subclass: `Frame` *(Inherits ProdukOptik)*
* **Atribut Tambahan:** `material` (e.g., Titanium, Asetat), `tipe_rim` (e.g., Full Rim, Rimless).
* **Overriding Method:** `tampil_detail()` menambahkan format `[material] ([tipe_rim])`.

#### C. Subclass: `Lensa` *(Inherits ProdukOptik)*
* **Atribut Tambahan:** `ukuran_lensa` (e.g., -2.00), `jenis_lensa` (e.g., Blueray, Photocromic).
* **Overriding Method:** `tampil_detail()` menambahkan format `[ukuran_lensa] ([jenis_lensa])`.

#### D. Subclass: `Aksesoris` *(Inherits ProdukOptik)*
* **Atribut Tambahan:** `jenis_aks` (e.g., Pembersih, Lap Kacamata), `ukuran` (e.g., 60ml, 15x15 cm).
* **Overriding Method:** `tampil_detail()` menambahkan format `[jenis_aks] ([ukuran])`.

#### E. Class: `Inventory`
* **Atribut Class:** `max_gudang` (default: 1000).
* **Atribut Instance:** `nama_cabang`, `daftar_barang` *(List Agregasi Objek)*, `__pin_akses` *(Private)*.
* **Method:** `tampil_stok()`, `tambah_produk()`, `pin_akses` (Getter & Setter 3-digit), `update_kapasitas_gdg()` *(Class Method)*.

#### F. Class: `Transaksi`
* **Atribut Class:** `transaksi_selesai`, `bonus` (Hardcase & Lap Microfiber).
* **Atribut Instance:** `id_transaksi`, `nama_pelanggan`, `item_pembelian`, `status_pembayaran`, `__total_bayar` *(Private)*.
* **Method:** `tambah_item_pembelian()`, `cetak_nota()` (memberikan bonus otomatis jika membeli produk `FRM` atau `LNS`), `total_bayar` (Getter & Setter).

</details>

<details>
<summary><h2> Panduan Pengujian Program</h2></summary>

Eksekusi pada blok `if __name__ == '__main__':` menjalankan skenario simulasi:

1. **Inisialisasi & Instansiasi Objek:**
   * Membuat 15 objek spesifik dari subclass `Frame`, `Lensa`, dan `Aksesoris`.
   * Menyiapkan instance cabang `Optik Cahaya Samarinda Central Plaza`.
2. **Pendaftaran & Output Tabel Inventaris:**
   * Memasukkan ke-15 produk ke dalam inventory cabang secara berurutan.
   * Memanggil `stok_cab1.tampil_stok()` untuk mengeksekusi overriding method `tampil_detail()` dari tiap subclass dalam format tabel rapi.
3. **Pemuatan Metode Class & Static:**
   * Menghitung potensi omset produk `Ray-Ban Wayfarer Classic` via `hitung_omset()`.
   * Memperbarui batas kapasitas gudang pusat menjadi `1500` unit via `update_kapasitas_gdg()`.
4. **Simulasi Transaksi Kasir & Bonus:**
   * Menambahkan item pembelian ke `transaksi1` untuk pelanggan **Nur Azizah**.
   * Memotong stok barang secara real-time di inventaris cabang.
   * Mencetak nota resmi lengkap dengan bonus otomatis kacamata.
5. **Pengujian Keamanan Setter (Encapsulation Validation):**
   * Pengujian sengaja memasukkan stok negatif (`-2`) dan harga negatif (`-50000`) untuk memastikan error handling bekerja.
   * Menguji PIN cabang dengan string (`'ABC'`) lalu mengubahnya ke PIN valid (`777`).
   * Menguji total bayar transaksi dengan nilai negatif (`-500`).

</details>

<details>
<summary><h2> Cara Menjalankan</h2></summary>

1. Pastikan **Python 3.10+** sudah terinstal di perangkat Anda.
2. Buka Terminal / Command Prompt dan arahkan ke direktori proyek:
   ```bash
   cd POSTTEST_PBO/posttest-2
   ```
3. Jalankan file program:
   ```bash
   python posttest-2.py
   ```

</details>