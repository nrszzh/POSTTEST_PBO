class ProdukOptik:
    nama_optik = 'Optik Cahaya'
    produk_terdaftar = 0
    kategori_produk = ['FRM', 'LNS', 'AKS']

    def __init__(self, id_sku, nama_produk, kategori, harga, stok):
        self.id_sku = id_sku
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.__harga = harga
        self.__stok = stok
        ProdukOptik.produk_terdaftar += 1

    @property
    def harga(self):
        return self.__harga

    @property
    def stok(self):
        return self.__stok

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            print('Harga harus lebih besar dari Rp 0')
        else:
            self.__harga = harga_baru

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            print(f'Stok {self.nama_produk} tidak boleh negatif')
        else: 
            self.__stok = stok_baru

    def tampil_detail(self):
        print(f'| [{self.id_sku:<15}] {self.nama_produk:<35} | Kat: {self.kategori:<5} | Harga: Rp{self.harga:<10,.0f} | Stok: {self.stok:<3} |')

    def kurangi_stok(self, jumlah):
        if jumlah <= self.__stok:
            self.__stok -= jumlah
            return True
        else:
            print(f'Stok {self.nama_produk} tidak cukup, (Sisa : {self.__stok})')
            return False

    @classmethod
    def buat_sku(cls, kat_code, merk_code, fitur_code, uk_code, nama_produk, harga, stok):
        sku_generated = f'{kat_code.upper()}-{merk_code.upper()}-{fitur_code.upper()}-{uk_code.upper()}'
        return cls(sku_generated, nama_produk, kat_code.upper(), harga, stok)

    @staticmethod
    def hitung_omset(nom_harga, qty_stok):
        return nom_harga * qty_stok


class Inventory:
    nama_sistem = 'Optik Inventory System'
    max_gudang = 1000
    lokasi_gudang = 'Gudang Pusat Samarinda'

    def __init__(self, nama_cabang):
        self.nama_cabang = nama_cabang
        self.daftar_barang = []
        self.__pin_akses = '018'

    def tampil_stok(self):
        print(f'\n===================== STOK OPTIK CAHAYA ({self.nama_cabang.upper()}) =========================')
        if not self.daftar_barang:
            print('Belum ada produk yang terdaftar')
        else:
            for produk in self.daftar_barang:
                produk.tampil_detail()
        print('=' * 104 + '\n')

    def tambah_produk(self, produk):
        self.daftar_barang.append(produk)
        print(f'Berhasil menambahkan {produk.nama_produk} ke inventory {self.nama_cabang}')

    @property
    def pin_akses(self):
        return self.__pin_akses

    @pin_akses.setter
    def pin_akses(self, pin_baru):
        pin = str(pin_baru)
        if len(pin) != 3 or not pin.isdigit():
            print('PIN harus 3 digit angka')
        else:
            self.__pin_akses = pin
            print('PIN berhasil diubah')

    @classmethod
    def update_kapasitas_gdg(cls, kapasitas_baru):
        if kapasitas_baru > 0:
            cls.max_gudang = kapasitas_baru
            print(f'Kapasitas Gudang Pusat diperbarui menjadi: {cls.max_gudang} unit')


class Transaksi:
    nama_optik = 'Optik Cahaya'
    transaksi_selesai = 0
    bonus = ['Kotak Kacamata Hardcase Optik Cahaya', 'Lap Kain Microfiber Premium']

    def __init__(self, id_transaksi, nama_pelanggan):
        self.id_transaksi = id_transaksi
        self.nama_pelanggan = nama_pelanggan
        self.item_pembelian = []
        self.status_pembayaran = 'Pending'
        self.__total_bayar = 0

    @property
    def total_bayar(self):
        return self.__total_bayar

    @total_bayar.setter
    def total_bayar(self, nilai_baru):
        if nilai_baru < 0:
            print('Total bayar tidak boleh bernilai negatif!')
        else:
            self.__total_bayar = nilai_baru

    def tambah_item_pembelian(self, produk, qty=1):
        if produk.kurangi_stok(qty):
            subtotal = produk.harga * qty
            self.item_pembelian.append({
                'produk': produk,
                'qty': qty,
                'subtotal': subtotal
            })
            self.__total_bayar += subtotal
            print(f'Ditambahkan ke {self.id_transaksi}: {produk.nama_produk} (x{qty})')

    def cetak_nota(self):
        print('\n' + '=' * 75)
        print(f'               NOTA PEMBELIAN - {Transaksi.nama_optik.upper()}')
        print('=' * 75)
        print(f'ID Transaksi : {self.id_transaksi}')
        print(f'Pelanggan    : {self.nama_pelanggan}')
        print('-' * 75)
        print(f"{'SKU CODE':<15} | {'ITEM':<35} | {'QTY':<3} | {'SUBTOTAL':<12}")
        print('-' * 75)
        kacamata = False
        for item in self.item_pembelian:
            prod = item['produk']
            print(f"{prod.id_sku:<15} | {prod.nama_produk:<35} | {item['qty']:<3} | Rp{item['subtotal']:<10,.0f}")
            if prod.kategori in ['FRM', 'LNS']:
                kacamata = True
        print('-' * 75)
        print(f'TOTAL BELANJA : Rp{self.total_bayar:,.0f}')
        if kacamata:
            print('[FREE BONUS]:')
            for bonus in Transaksi.bonus:
                print(f'  + 1x {bonus}')
        print('=' * 75 + '\n')
        Transaksi.transaksi_selesai += 1

