class Mahasiswa:
    def __init__(self, nama, nim, program_studi, nilai):
        self.nama = nama
        self.nim = nim
        self.program_studi = program_studi
        self.nilai = nilai

class DataMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, nama, nim, program_studi, nilai):
        mahasiswa = Mahasiswa(nama, nim, program_studi, nilai)
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_mahasiswa(self):
        if not self.daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        for mahasiswa in self.daftar_mahasiswa:
            print(f"Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Program Studi: {mahasiswa.program_studi}, Nilai: {mahasiswa.nilai}")

    def hitung_rata_rata_nilai(self):
        if not self.daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        total_nilai = sum(mahasiswa.nilai for mahasiswa in self.daftar_mahasiswa)
        rata_rata = total_nilai / len(self.daftar_mahasiswa)
        print(f"Rata-rata Nilai: {rata_rata:.2f}")

    def cari_nilai_tertinggi_dan_terendah(self):
        if not self.daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        tertinggi = max(self.daftar_mahasiswa, key=lambda m: m.nilai)
        terendah = min(self.daftar_mahasiswa, key=lambda m: m.nilai)
        print(f"Mahasiswa dengan nilai tertinggi: {tertinggi.nama}, Nilai: {tertinggi.nilai}")
        print(f"Mahasiswa dengan nilai terendah: {terendah.nama}, Nilai: {terendah.nilai}")

class Barang:
    def __init__(self, nama_barang, kode_barang, jumlah_barang):
        self.nama = nama_barang
        self.kode = kode_barang
        self.jumlah = jumlah_barang

class Inventaris:
    def __init__(self):
        self.daftar_barang = []

    def tambah_barang(self, nama_barang, kode_barang, jumlah_barang):
        barang = Barang(nama_barang, kode_barang, jumlah_barang)
        self.daftar_barang.append(barang)
        print(f"Barang '{nama_barang}' dengan kode '{kode_barang}' telah ditambahkan.")

    def tampilkan_semua_barang(self):
        if not self.daftar_barang:
            print("Tidak ada barang dalam inventaris.")
            return
        for barang in self.daftar_barang:
            print(f"Nama: {barang.nama}, Kode: {barang.kode}, Jumlah: {barang.jumlah}")

    def cari_barang_berdasarkan_kode(self, kode_barang):
        for barang in self.daftar_barang:
            if barang.kode == kode_barang:
                print(f"Barang ditemukan - Nama: {barang.nama}, Kode: {barang.kode}, Jumlah: {barang.jumlah}")
                return barang
        print(f"Barang dengan kode '{kode_barang}' tidak ditemukan.")
        return None

    def hapus_barang_berdasarkan_kode(self, kode_barang):
        barang = self.cari_barang_berdasarkan_kode(kode_barang)
        if barang:
            self.daftar_barang.remove(barang)
            print(f"Barang dengan kode '{kode_barang}' telah dihapus.")

class Transaksi:
    def __init__(self, jenis, jumlah, keterangan):
        self.jenis = jenis  # 'deposit' atau 'withdraw'
        self.jumlah = jumlah
        self.keterangan = keterangan

    def __str__(self):
        return f"Jenis: {self.jenis}, Jumlah: {self.format_rupiah(self.jumlah)}, Keterangan: {self.keterangan}"

    @staticmethod
    def format_rupiah(jumlah):
        return f"RP {jumlah:,.2f}".replace(",", ".").replace(".", ",", 1)

class KeuanganPribadi:
    def __init__(self):
        self.daftar_transaksi = []

    def tambah_transaksi(self, jenis, jumlah, keterangan):
        transaksi = Transaksi(jenis, jumlah, keterangan)
        self.daftar_transaksi.append(transaksi)
        print(f"Transaksi '{jenis}' sebesar {Transaksi.format_rupiah(jumlah)} telah ditambahkan.")

    def tampilkan_semua_transaksi(self):
        if not self.daftar_transaksi:
            print("Tidak ada transaksi yang tercatat.")
            return
        for transaksi in self.daftar_transaksi:
            print(transaksi)

    def hitung_total_deposit(self):
        total_deposit = sum(transaksi.jumlah for transaksi in self.daftar_transaksi if transaksi.jenis == 'deposit')
        print(f"Total Deposit: {Transaksi.format_rupiah(total_deposit)}")
        return total_deposit

    def hitung_total_withdraw(self):
        total_withdraw = sum(transaksi.jumlah for transaksi in self.daftar_transaksi if transaksi.jenis == 'withdraw')
        print(f"Total Withdraw: {Transaksi.format_rupiah(total_withdraw)}")
        return total_withdraw

    def hitung_saldo_akhir(self):
        total_deposit = self.hitung_total_deposit()
        total_withdraw = self.hitung_total_withdraw()
        saldo_akhir = total_deposit - total_withdraw
        print(f"Saldo Akhir: {Transaksi.format_rupiah(saldo_akhir)}")
        return saldo_akhir

def main():
    data_mahasiswa = DataMahasiswa()
    inventaris = Inventaris()
    keuangan = KeuanganPribadi()
    
    while True:
        print("\nMenu:")
        print("1. Kelola Data Mahasiswa")
        print("2. Kelola Inventaris Barang")
        print("3. Kelola Keuangan Pribadi")
        print("4. Keluar")

        pilihan_utama = input("Pilih menu: ").strip()

        if pilihan_utama == '1':
            while True:
                print("\nMenu:")
                print("1. Tambah data mahasiswa")
                print("2. Tampilkan data mahasiswa")
                print("3. Hitung rata-rata nilai")
                print("4. Cari nilai tertinggi dan terendah")
                print("5. Kembali ke Menu Utama")

                pilihan = input("Pilih menu: ")

                if pilihan == '1':
                    nama = input("Masukkan nama: ")
                    nim = input("Masukkan NIM: ")
                    program_studi = input("Masukkan program studi: ")
                    nilai = float(input("Masukkan nilai: "))
                    data_mahasiswa.tambah_mahasiswa(nama, nim, program_studi, nilai)
                elif pilihan == '2':
                    data_mahasiswa.tampilkan_mahasiswa()
                elif pilihan == '3':
                    data_mahasiswa.hitung_rata_rata_nilai()
                elif pilihan == '4':
                    data_mahasiswa.cari_nilai_tertinggi_dan_terendah()
                elif pilihan == '5':
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan_utama == '2':
            while True:
                print("\nMenu:")
                print("1. Tambah barang")
                print("2. Tampilkan semua barang")
                print("3. Cari barang berdasarkan kode")
                print("4. Hapus barang berdasarkan kode")
                print("5. Kembali ke Menu Utama")

                pilihan = input("Pilih menu: ")

                if pilihan == '1':
                    nama_barang = input("Masukkan nama barang: ")
                    kode_barang = input("Masukkan kode barang: ")
                    jumlah_barang = int(input("Masukkan jumlah barang: "))
                    inventaris.tambah_barang(nama_barang, kode_barang, jumlah_barang)
                elif pilihan == '2':
                    inventaris.tampilkan_semua_barang()
                elif pilihan == '3':
                    kode_barang = input("Masukkan kode barang yang dicari: ")
                    inventaris.cari_barang_berdasarkan_kode(kode_barang)
                elif pilihan == '4':
                    kode_barang = input("Masukkan kode barang yang akan dihapus: ")
                    inventaris.hapus_barang_berdasarkan_kode(kode_barang)
                elif pilihan == '5':
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan_utama == '3':
            while True:
                print("\nMenu:")
                print("1. Tambah transaksi")
                print("2. Tampilkan semua transaksi")
                print("3. Hitung total deposit")
                print("4. Hitung total withdraw")
                print("5. Hitung saldo akhir")
                print("6. Kembali ke Menu Utama")

                pilihan = input("Pilih menu: ")

                if pilihan == '1':
                    jenis = input("Masukkan jenis transaksi (deposit/withdraw): ").strip().lower()
                    if jenis not in ['deposit', 'withdraw']:
                        print("Jenis transaksi tidak valid. Silakan masukkan 'deposit' atau 'withdraw'.")
                        continue
                    jumlah = float(input("Masukkan jumlah: "))
                    keterangan = input("Masukkan keterangan: ")
                    keuangan.tambah_transaksi(jenis, jumlah, keterangan)
                elif pilihan == '2':
                    keuangan.tampilkan_semua_transaksi()
                elif pilihan == '3':
                    keuangan.hitung_total_deposit()
                elif pilihan == '4':
                    keuangan.hitung_total_withdraw()
                elif pilihan == '5':
                    keuangan.hitung_saldo_akhir()
                elif pilihan == '6':
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan_utama == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
