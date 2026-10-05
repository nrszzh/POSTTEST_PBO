class ProdukOptik:
    nama_optik = 'Optik Cahaya'
    produk_terdaftar = 0

    def __init__(self, id_sku, nama_produk, kategori, harga, stok):
        self.id_sku = id_sku
        self.nama_produk = nama_produk
        self.kategori = kategori
        self._harga = harga
        self._stok = stok
        ProdukOptik.produk_terdaftar += 1

    @property
    def harga(self):
        return self._harga

    @property
    def stok(self):
        return self._stok

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            print('Harga harus lebih besar dari Rp 0')
        else:
            self._harga = harga_baru

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            print(f'Stok {self.nama_produk} tidak boleh negatif')
        else: 
            self._stok = stok_baru

    def tampil_detail(self):
        print(f' [{self.id_sku:<15}] | {self.nama_produk:<35} | {self.kategori:<8} | Rp{self.harga:<10,.0f} | {self.stok:<3} ', end= "")

    def kurangi_stok(self, jumlah):
        if jumlah <= self._stok:
            self._stok -= jumlah
            return True
        else:
            print(f'Stok {self.nama_produk} tidak cukup, (Sisa : {self._stok})')
            return False

    @staticmethod
    def hitung_omset(nom_harga, qty_stok):
        return nom_harga * qty_stok


class Frame(ProdukOptik):
    def __init__(self, id_sku, nama_produk, harga, stok, material, tipe_rim):
        super().__init__(id_sku, nama_produk, 'FRM', harga, stok)
        self.material = material
        self.tipe_rim = tipe_rim 

    def tampil_detail(self):
        super().tampil_detail() 
        spec = f'{self.material} ({self.tipe_rim})'
        print(f' | {spec:<25} |')


class Lensa(ProdukOptik):
    def __init__(self, id_sku, nama_produk, harga, stok, ukuran_lensa, jenis_lensa):
        super().__init__(id_sku, nama_produk, 'LNS', harga, stok)
        self.ukuran_lensa = ukuran_lensa
        self.jenis_lensa = jenis_lensa

    def tampil_detail(self):
        super().tampil_detail() 
        spec = f'{self.ukuran_lensa} ({self.jenis_lensa})'
        print(f' | {spec:<25} |')

class Aksesoris(ProdukOptik):
    def __init__(self, id_sku, nama_produk, harga, stok, jenis_aks, ukuran):
        super().__init__(id_sku, nama_produk, 'AKS', harga, stok)
        self.jenis_aks = jenis_aks
        self.ukuran = ukuran

    def tampil_detail(self):
        super().tampil_detail() 
        spec = f'{self.jenis_aks} ({self.ukuran})'
        print(f' | {spec:<25} |')


class Inventory:
    max_gudang = 1000

    def __init__(self, nama_cabang):
        self.nama_cabang = nama_cabang
        self.daftar_barang = []
        self.__pin_akses = '018'

    def tampil_stok(self):
        print(f"\n=======================================================================================================================")
        print(f" { 'SKU CODE':<18}| {'NAMA PRODUK':<35} | {'KATEGORI':<8} | {'HARGA':<12} | {'STOK':<3} | {'SPESIFIKASI':<25} |")
        print("-" * 119)
        
        for produk in self.daftar_barang:
            produk.tampil_detail()
        print("=" * 119 + "\n")

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
        print(f'                    NOTA PEMBELIAN - {ProdukOptik.nama_optik.upper()}')
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
    produk1 = Frame('FRM-RB-BLK-52', 'Ray-Ban Wayfarer Classic', 2200000, 5, 'Titanium', 'Full Rim')
    produk2 = Frame('FRM-OAK-GRY-55', 'Oakley Crosslink Pitch', 1850000, 8, 'Asetat', 'Half Rim')
    produk3 = Frame('FRM-GU-GLD-50', 'Gucci Round Vintage Gold', 3100000, 3, 'Monel Metal', 'Full Rim')
    produk4 = Frame('FRM-VO-SLV-51', 'Vogue Metal Cat-Eye', 1400000, 6, 'Stainless Steel', 'Rimless')
    produk5 = Frame('FRM-PE-BRN-53', 'Persol Cellor Matte Brown', 2750000, 4, 'Asetat Wood', 'Full Rim')
    produk6 = Lensa('LNS-ES-BLR-0200', 'Essilor Crizal BlueRock', 1200000, 10, '-2,00', 'Blueray')
    produk7 = Lensa('LNS-HO-TRN-0150', 'Hoya Sensity Transitions', 1650000, 12, '-1,50', 'Photocromic')
    produk8 = Lensa('LNS-ZE-DRV-0300', 'Zeiss DriveSafe Precision', 2800000, 4, '-3,00', 'Anti-Glare')
    produk9 = Lensa('LNS-RO-PLS-0100', 'Rodenstock Cosmolit Plus', 950000, 7, '+1,00', 'Progressive')
    produk10 = Lensa('LNS-NIK-SGL-000', 'Nikon Single Vision Clear', 650000, 15, '0,00', 'Anti-UV')
    produk11 = Aksesoris('AKS-OPC-LIQ-60', 'OptiClean Spray Solution', 35000, 25, 'Pembersih', '60ml')
    produk12 = Aksesoris('AKS-MIC-PRF-01', 'Microfiber Premium Cloth', 15000, 50, 'Lap Kacamata', '15x15 cm')
    produk13 = Aksesoris('AKS-HCS-LEA-02', 'Hardcase Leather Protection', 75000, 15, 'Kotak', 'Standard')
    produk14 = Aksesoris('AKS-STR-SIL-03', 'Silicone Sports Strap', 25000, 30, 'Tali Gantung', '60 cm')
    produk15 = Aksesoris('AKS-NSP-CLR-05', 'Nosepad Air Cushion Set', 20000, 40, 'Sparepart', '10 Pairs')


    stok_cab1 = Inventory('Optik Cahaya Samarinda Central Plaza')
    stok_cab2 = Inventory('Optik Cahaya Bontang City Mall')

    transaksi1 = Transaksi('TR-0001', 'Nur Azizah')
    transaksi2 = Transaksi('TR-0002', 'Islamiyah')

    daftar_produk = [
        produk1, produk2, produk3, produk4, produk5,
        produk6, produk7, produk8, produk9, produk10,
        produk11, produk12, produk13, produk14, produk15
    ]
    
    for p in daftar_produk:
        stok_cab1.tambah_produk(p)
    stok_cab1.tampil_stok()

    omset_p1 = ProdukOptik.hitung_omset(produk1.harga, produk1.stok)
    print(f'Omset dari {produk1.nama_produk}: Rp{omset_p1:,.0f} \n')

    Inventory.update_kapasitas_gdg(1500)

    print()
    transaksi1.tambah_item_pembelian(produk1, qty=1)
    transaksi1.tambah_item_pembelian(produk2, qty=1)
    transaksi1.tambah_item_pembelian(produk3, qty=2)
    transaksi1.cetak_nota()

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