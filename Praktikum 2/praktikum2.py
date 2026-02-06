# ========================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   1: Membuat Fungsi Load Data dari File
# ========================================================================

# Variabel menyimpan data file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} # Inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() # Ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") # Ambil data per item data
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)} # Masukkan dalam dictionary
    return data_dict

buka_data = baca_data(nama_file) # Memanggil fungsi load data dan menyimpan dalam variabel
print("jumlah data terbaca", len(buka_data)) # Melihat berapa data yang di load

# ========================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   2: Membuat Fungsi Menampilkan Data
# ========================================================================
def tampilkan_data(data_dict):
    # Membuat header tabel
    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM' :<10} | {'Nama' :<12} | {'Nilai' :>5}")
    """
    untuk tampilan yang rapi, atur lebar kolom
    {'NIM' :<10} artinya nim rata kiri dengan lebar kolom 10 karakter
    {'Nama' :<12} artinya nama rata kiri dengan lebar kolom 12 karakter
    {'Nilai' :>5} artinya nilai rata kanan dengan lebar kolom 5 
    """
    print("-"*35) # Membuat garis

    # Menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")

tampilkan_data(buka_data) # Memanggil fungsi untuk menampilkan data

# ========================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   3: Membuat Fungsi dan Mencari Data
# ========================================================================

def cari_data(data_dict):
    # Pencarian data berdasarkan nim sebagai key dictionary
    # Membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("====== Data Mahasiswa Ditemukan ======")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

# Memanggil fungsi cari data
cari_data(buka_data)

# ========================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   4: Membuat Fungsi Update Data
# ========================================================================

# Membuat fungsi update data
def ubah_data(data_dict):

    # Awali dulu dengan mencari nim / data mahasiswa yang ingin di update
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ").strip()
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus diantara 0 dan 100. Update Dibatalkan")
        return

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi nilai {nilai_baru}")

# Memanggil fungsi ubah data
ubah_data(buka_data)

# ========================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   5: Membuat Fungsi Menyimpan Data pada File
# ========================================================================

# Membuat fungsi menyimpan data ke File
def simpan_data(nama_file, data_dict):
    with open(nama_file,"w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai}\n")

# Memanggil fungsi simpan data
simpan_data(nama_file, buka_data)
print("\nData Berhasil Disimpan ke file:", nama_file)

# ========================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan   6: Membuat Menu Interaktif
# ========================================================================

def main():
    # Load data otomatis saat program dimulai
    buka_data = baca_data(nama_file) #fs.1

    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)

        elif pilihan == "2":
            cari_data(buka_data)

        elif pilihan == "3":
            ubah_data(buka_data)
        
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data berhasil Disimpan")
        
        elif pilihan == "0":
            print("Program Selesai.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi")

if __name__ == "__main__":
    main()