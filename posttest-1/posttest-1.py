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


if __name__ == '__main__':
    produk1 = ProdukOptik('FRM-RB-BLK-52', 'Frame Ray-Ban Wayfarer Black', 'FRM', 2200000, 5)
    produk2 = ProdukOptik.buat_sku('LNS', 'ES', 'BLR', '0200', 'Lensa Essilor BlueRay Minus 2.00', 1200000, 10)
    produk3 = ProdukOptik('AKS-OPC-LIQ-60', 'Cairan Pembersih OptiClean 60ml', 'AKS', 35000, 20)

    stok_cab1 = Inventory('Optik Cahaya Samarinda Central Plaza')
    stok_cab2 = Inventory('Optik Cahaya Bontang City Mall')

    transaksi1 = Transaksi('TR-0001', 'Nur Azizah')
    transaksi2 = Transaksi('TR-0002', 'Islamiyah')


    stok_cab1.tambah_produk(produk1)
    stok_cab1.tambah_produk(produk2)
    stok_cab1.tambah_produk(produk3)
    stok_cab1.tampil_stok()

    omset_p1 = ProdukOptik.hitung_omset(produk1.harga, produk1.stok)
    print(f'Omset dari {produk1.nama_produk}: Rp{omset_p1:,.0f} \n')

    Inventory.update_kapasitas_gdg(1500)

    print()
    transaksi1.tambah_item_pembelian(produk1, qty=1)
    transaksi1.tambah_item_pembelian(produk2, qty=1)
    transaksi1.tambah_item_pembelian(produk3, qty=2)
    transaksi1.cetak_nota()
    
    stok_cab1.tampil_stok()


    produk1.stok = -2
    produk1.stok = 10
    produk1.harga = -50000
    produk1.harga = 545000
    print(f'Stok {produk1.nama_produk}: {produk1.stok}')
    print(f'Harga {produk1.nama_produk}: Rp{produk1.harga:,.0f}')

    stok_cab1.pin_akses = 'ABC' 
    stok_cab1.pin_akses = 777

    transaksi1.total_bayar = -500 
    transaksi1.total_bayar = 3000000 
    print(f'Total bayar TR-001: Rp{transaksi1.total_bayar:,.0f}')