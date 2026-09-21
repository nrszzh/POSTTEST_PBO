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


class Inventory:
    nama_sistem = 'Optik Inventory System'
    max_gudang = 1000
    lokasi_gudang = 'Gudang Pusat Samarinda'

    def __init__(self, nama_cabang):
        self.nama_cabang = nama_cabang
        self.daftar_barang = []
        self.__pin_akses = '018'



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


