from abc import ABC, abstractmethod
from datetime import datetime

class ProdukOptik(ABC):
    nama_optik = 'Optik Cahaya'
    produk_terdaftar = 0
    dapat_bonus = False

    def __init__(self, id_sku, nama_produk, kategori, harga, stok, diskon=0.0):
        self.id_sku = id_sku
        self.nama_produk = nama_produk
        self.kategori = kategori
        self._harga = harga
        self._stok = stok
        self.diskon = diskon
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
            print(' [!] Harga harus lebih besar dari Rp 0')
        else:
            self._harga = harga_baru

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            print(f' [!] Stok {self.nama_produk} tidak boleh negatif')
        else: 
            self._stok = stok_baru

    def tampil_detail(self):
        print(f' [{self.id_sku:<15}] | {self.nama_produk:<35} | {self.kategori:<8} | Rp{self.hitung_harga_akhir():<10,.0f} | {self.stok:<4} | {self.spesifikasi():<25} |')

    def kurangi_stok(self, jumlah):
        if jumlah <= self._stok:
            self._stok -= jumlah
            return True
        else:
            print(f' [!] Stok {self.nama_produk} tidak cukup, (Sisa : {self._stok})')
            return False

    @staticmethod
    def hitung_omset(nom_harga, qty_stok):
        return nom_harga * qty_stok

    @abstractmethod
    def hitung_harga_akhir(self):
        pass

    @abstractmethod
    def spesifikasi(self):
        pass

    def __add__(self, other):
        if hasattr(other, 'hitung_harga_akhir'):
            return self.hitung_harga_akhir() + other.hitung_harga_akhir()
        if isinstance(other, (int, float)):
            return self.hitung_harga_akhir() + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return other + self.hitung_harga_akhir()
        return NotImplemented



class Frame(ProdukOptik):
    dapat_bonus = True

    def __init__(self, id_sku, nama_produk, harga, stok, material, tipe_rim, diskon=0.0):
        super().__init__(id_sku, nama_produk, 'FRM', harga, stok, diskon)
        self.material = material
        self.tipe_rim = tipe_rim 

    def hitung_harga_akhir(self):
        harga_setelah_diskon = self._harga * (1 - self.diskon)
        return harga_setelah_diskon

    def spesifikasi(self):
        return f'{self.material} ({self.tipe_rim})'


class Lensa(ProdukOptik):
    dapat_bonus = True
    ganti_jenis = {
        'Anti UV' :    0,
        'Anti-Glare':  50_000,
        'Blueray':     150_000,
        'Photocromic': 300_000,
        'Progressive': 500_000,
    }

    def __init__(self, id_sku, nama_produk, harga, stok, ukuran_lensa, jenis_lensa, diskon=0.0):
        super().__init__(id_sku, nama_produk, 'LNS', harga, stok, diskon)
        self.ukuran_lensa = ukuran_lensa
        self.jenis_lensa = jenis_lensa

    def hitung_harga_akhir(self):
        ganti = self.ganti_jenis.get(self.jenis_lensa, 0)
        harga_dasar_lensa = self._harga + ganti
        return harga_dasar_lensa * (1 - self.diskon)

    def spesifikasi(self):
        return f'{self.ukuran_lensa} ({self.jenis_lensa})'

class Aksesoris(ProdukOptik):
    def __init__(self, id_sku, nama_produk, harga, stok, jenis_aks, ukuran, diskon=0.0):
        super().__init__(id_sku, nama_produk, 'AKS', harga, stok, diskon)
        self.jenis_aks = jenis_aks
        self.ukuran = ukuran

    def hitung_harga_akhir(self):
        return self._harga * (1 - self.diskon)

    def spesifikasi(self):
        return f'{self.jenis_aks} ({self.ukuran})'

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
        print(f' [+] Berhasil menambahkan {produk.nama_produk} ke inventory {self.nama_cabang}')

    @property
    def pin_akses(self):
        return self.__pin_akses

    @pin_akses.setter
    def pin_akses(self, pin_baru):
        pin = str(pin_baru)
        if len(pin) != 3 or not pin.isdigit():
            print(' [!] PIN harus 3 digit angka')
        else:
            self.__pin_akses = pin
            print(' [~] PIN berhasil diubah')

    @classmethod
    def update_kapasitas_gdg(cls, kapasitas_baru):
        if kapasitas_baru > 0:
            cls.max_gudang = kapasitas_baru
            print(f' [~] Kapasitas Gudang Pusat diperbarui menjadi: {cls.max_gudang} unit')

class DetailTransaksi:
    """Kelas komposisi yang siklus hidupnya terikat di dalam Transaksi."""
    def __init__(self, produk, qty):
        self.produk = produk
        self.qty = qty
        self.subtotal = produk.hitung_harga_akhir() * qty

class Transaksi:
    transaksi_selesai = 0
    bonus = ['Kotak Kacamata Hardcase Optik Cahaya', 'Lap Kain Microfiber Premium']

    def __init__(self, id_transaksi, nama_pelanggan):
        self.id_transaksi = id_transaksi
        self.nama_pelanggan = nama_pelanggan
        self.item_pembelian = []
        self.item_layanan = []
        self.status_pembayaran = 'Pending'
        self.__total_bayar = 0
        self.total_potongan = 0

    @property
    def total_bayar(self):
        return self.__total_bayar

    @total_bayar.setter
    def total_bayar(self, nilai_baru):
        if nilai_baru < 0:
            print(' [!] Total bayar tidak boleh bernilai negatif!')
        else:
            self.__total_bayar = nilai_baru

    def tambah_item_pembelian(self, produk, qty=1):
        if produk.kurangi_stok(qty):
            item_detail = DetailTransaksi(produk, qty)
            self.item_pembelian.append(item_detail)
            harga_kotor = (produk._harga if not isinstance(produk, Lensa) else (produk._harga + produk.ganti_jenis.get(produk.jenis_lensa, 0))) * qty
            potongan_item = harga_kotor - item_detail.subtotal
            self.total_potongan += potongan_item
            self.__total_bayar += item_detail.subtotal
            print(f' [+] Ditambahkan ke {self.id_transaksi}: {produk.nama_produk} (x{qty})')

    def tambah_layanan(self, data_layanan):
        self.item_layanan.append(data_layanan)
        self.__total_bayar += data_layanan['biaya']
        print(f" [+] {data_layanan['kategori_layanan']} ({data_layanan['keterangan']}) biaya Rp{data_layanan['biaya']:,.0f}")

    def cetak_nota(self, nama_cabang):
        waktu_sekarang = datetime.now()
        waktu_transaksi = waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S WITA')
        jam = waktu_sekarang.hour

        if 8 <= jam < 15:
            nama_kasir = "Meidiana"
        else:
            nama_kasir = "Dewi"

        print('\n' + '=' * 95)
        print(f'NOTA PEMBELIAN - {nama_cabang.upper()}'.center(95))
        print('=' * 95)
        print(f'ID Transaksi     : {self.id_transaksi}')
        print(f'Pelanggan        : {self.nama_pelanggan}')
        print('=' * 95)
        ada_bonus = False

        if self.item_pembelian:
            print('\n[PEMBELIAN PRODUK]')
            print(f"{'SKU CODE':<18}   {'ITEM PRODUK':<30}   {'HARGA':<15}   {'QTY':<5}   {'SUBTOTAL':<15}")
            print('-' * 95)
            for item in self.item_pembelian:
                prod = item.produk
                if isinstance(prod, Lensa):
                    surcharge = prod.ganti_jenis.get(prod.jenis_lensa, 0)
                    harga_tampil = prod._harga + surcharge
                else:
                    harga_tampil = prod._harga
                subtotal_tampil = harga_tampil * item.qty
                print(f"{prod.id_sku:<18}   {prod.nama_produk:<30}   Rp {harga_tampil:<12,.0f}   {item.qty:<5}   Rp {subtotal_tampil:<12,.0f}")
                if prod.dapat_bonus:
                    ada_bonus = True

        if self.item_layanan:
            if self.item_pembelian:
                print('-' * 95)
            print('\n[LAYANAN OPTIK]')
            print(f"{'KATEGORI LAYANAN':<18}   {'KETERANGAN':<56}   {'BIAYA':<10}")
            print('-' * 95)
            for item in self.item_layanan:
                print(f"{item['kategori_layanan']:<18}   {item['keterangan']:<56}   Rp {item['biaya']:<10,.0f}")

        print('-' * 95)
        if ada_bonus:
            print('\n[FREE BONUS]:')
            for b in Transaksi.bonus:
                print(f'  + 1x {b}')

        print('-' * 95)
        print(f"{'':<60} POTONGAN HARGA   : Rp {self.total_potongan:<12,.0f}")
        print(f"{'':<60} TOTAL PEMBAYARAN : Rp {self.total_bayar:<12,.0f}")
        
        print('=' * 95)
        print(f'Kasir : {nama_kasir}     -     Waktu : {waktu_transaksi}'.center(95))
        print('=' * 95)
        Transaksi.transaksi_selesai += 1

class LayananPemeriksaanMata:
    def __init__(self, jenis_pemeriksaan, biaya):
        self.jenis_pemeriksaan = jenis_pemeriksaan
        self.biaya = biaya

    def dilayani(self):
        return {
            'kategori_layanan': 'Pemeriksaan Mata',
            'keterangan': self.jenis_pemeriksaan,
            'biaya': self.biaya
        }

class LayananPasangLensa:
    def __init__(self, keterangan, biaya):
        self.keterangan = keterangan
        self.biaya = biaya

    def dilayani(self):
        return {
            'kategori_layanan': 'Pemasangan Lensa',
            'keterangan': self.keterangan,
            'biaya': self.biaya
        }

def layanan_optik(daftar_layanan, objek_transaksi):
    for layanan in daftar_layanan:
        data_hasil = layanan.dilayani()
        objek_transaksi.tambah_layanan(data_hasil)

if __name__ == '__main__':
    print("\n1: INSTANSIASI PRODUK, INVENTORY, TRANSAKSI")
    print("-" * 45)
    produk1  = Frame('FRM-RB-BLK-52', 'Ray-Ban Wayfarer Classic', 2200000, 5, 'Titanium', 'Full Rim', diskon=0.1)  
    produk2  = Frame('FRM-OAK-GRY-55','Oakley Crosslink Pitch', 1850000, 8, 'Asetat', 'Half Rim')                 
    produk3  = Frame('FRM-GU-GLD-50','Gucci Round Vintage Gold', 3100000, 3, 'Monel Metal', 'Full Rim', diskon=0.15) 
    produk4  = Frame('FRM-VO-SLV-51', 'Vogue Metal Cat-Eye', 1400000, 6, 'Stainless Steel', 'Rimless')         
    produk5  = Frame('FRM-PE-BRN-53', 'Persol Cellor Matte Brown', 2750000, 4, 'Asetat Wood', 'Full Rim')            
    produk6  = Lensa('LNS-ES-BLR-0200', 'Essilor Crizal BlueRock', 1200000, 10, '-2,00', 'Blueray', diskon=0.05)  
    produk7  = Lensa('LNS-HO-TRN-0150', 'Hoya Sensity Transitions', 1650000, 12, '-1,50', 'Photocromic')                
    produk8  = Lensa('LNS-ZE-DRV-0300', 'Zeiss DriveSafe Precision', 2800000, 4, '-3,00', 'Anti-Glare', diskon=0.2)   
    produk9  = Lensa('LNS-RO-PLS-0100', 'Rodenstock Cosmolit Plus', 950000,  7, '+1,00', 'Progressive')               
    produk10 = Lensa('LNS-NIK-SGL-000', 'Nikon Single Vision Clear', 650000,  15, '0,00', 'Anti-UV')                    
    produk11 = Aksesoris('AKS-OPC-LIQ-60', 'OptiClean Spray Solution', 35000, 25, 'Pembersih', '60ml')                 
    produk12 = Aksesoris('AKS-MIC-PRF-01', 'Microfiber Premium Cloth', 15000, 50, 'Lap Kacamata', '15x15 cm')           
    produk13 = Aksesoris('AKS-HCS-LEA-02', 'Hardcase Leather Protection', 75000, 15, 'Kotak', 'Standard', diskon=0.1)
    produk14 = Aksesoris('AKS-STR-SIL-03', 'Silicone Sports Strap', 25000, 30, 'Tali Gantung', '60 cm')               
    produk15 = Aksesoris('AKS-NSP-CLR-05', 'Nosepad Air Cushion Set', 20000, 40, 'Sparepart', '10 Pairs')               

    daftar_produk = [produk1, produk2, produk3, produk4, produk5,
                    produk6, produk7, produk8, produk9, produk10,
                    produk11, produk12, produk13, produk14, produk15]

    stok_cab1 = Inventory('Optik Cahaya Samarinda Central Plaza')
    stok_cab2 = Inventory('Optik Cahaya Bontang City Mall')

    for p in daftar_produk:
        stok_cab1.tambah_produk(p)

    transaksi1 = Transaksi('TR-0001', 'Nur Azizah')
    transaksi2 = Transaksi('TR-0002', 'Islamiyah')
    transaksi1.tambah_item_pembelian(produk1, qty=1)
    transaksi1.tambah_item_pembelian(produk2, qty=1)
    transaksi1.tambah_item_pembelian(produk3, qty=2)


    print("\n2: PEMANGGILAN METHOD, DUCK TYPING & MAGIC METHOD")
    print("-" * 50)
    omset_p1 = ProdukOptik.hitung_omset(produk1.harga, produk1.stok)
    print(f'-> Static Method:')
    print(f' [~] Omset {produk1.nama_produk}): Rp{omset_p1:,.0f}')
    print(f'\n-> Class Method:')
    Inventory.update_kapasitas_gdg(1500)

    periksa_lengkap = LayananPemeriksaanMata('Skrining Lengkap & Konsultasi Dokter', 150000) 
    pasang  = LayananPasangLensa('Pasang Lensa (Lensa Sendiri)', 50000)
    print('\n-> Uji Duck Typing (Layanan Optik):')
    layanan_optik([periksa_lengkap, pasang], transaksi1)

    print('\n-> Uji Magic Method (__add__ & __radd__):')
    cek1 = produk1 + produk6
    print(f' [~] Total Harga 2 produk      : Rp{cek1:,.0f}')
    cek2 = produk1 + produk7 + produk11
    print(f' [~] Total Harga 3 produk      : Rp{cek2:,.0f}')
    cek4 = sum([produk1, produk6, produk11, produk12])
    print(f' [~] Total Harga Paket         : Rp{cek4:,.0f}')


    print("\n3: VALIDASI ENKAPSULASI & TRY-EXCEPT")
    print("-" * 36)
    
    print('-> Uji Setter (Stok & Harga Negatif):')
    produk1.stok = -2
    produk1.stok = 10
    produk1.harga = -50000
    produk1.harga = 545000
    print(f' [~] Stok {produk1.nama_produk} : {produk1.stok} unit')
    print(f' [~] Harga {produk1.nama_produk}: Rp{produk1.harga:,.0f}')

    print('\n-> Uji Setter PIN Akses Inventory:')
    stok_cab1.pin_akses = 'ABC' 
    stok_cab1.pin_akses = 777

    print('\n-> Uji Setter Total Bayar Transaksi:')
    transaksi_uji = Transaksi('TR-TEST', 'Dummy Mummy')
    transaksi_uji.total_bayar = -500 
    transaksi_uji.total_bayar = 3000000 
    print(f' [~] Total bayar valid : Rp{transaksi_uji.total_bayar:,.0f}')

    print('\n-> Uji Try-Except Instansiasi Abstract Class (ProdukOptik):')
    try:
        p_abc = ProdukOptik('TST-018', 'Produk Absctract', 'OPT', 100000, 2)
        print(f' {p_abc}')
    except TypeError as e:
        print(f' [!] {e}')


    print("\n4: TAMPILAN STOK")
    print("-" * 15)
    stok_cab1.tampil_stok()


    print("\n5: TAMPILAN STRUK TRANSAKSI")
    print("-" * 30)
    transaksi1.cetak_nota("Optik Cahaya Samarinda Central Plaza")