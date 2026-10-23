
    def tampil_detail(self):
        super().tampil_detail() 
        spec = f'{self.jenis_aks} ({self.ukuran})'
        print(f' | {spec:<25} |')
