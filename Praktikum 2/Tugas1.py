# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Azzam Prastianto
# NIM : J0403251153
# Kelas : A2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"
# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------

def baca_stok(nama_file): # Kita membuat fungsi baca_stok()
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
    - stok_dict (dictionary)
    key = kode_barang
    value = {"nama": nama_barang, "stok": stok_int}
    """

   # TODO: Buka file dan baca seluruh baris
    stok_dict = {} # Kita definisikan sebagai dictionary
    try: # Coba jika filenya ada atau tidak
        with open(nama_file, "r", encoding="utf-8") as file: # Kita membuka dan membaca file 
            for baris in file: # Kita membaca filenya satu per satu
                baris = baris.strip() # Kita ubah barisnya agar \n hilang
                KodeBarang, NamaBarang, Stok = baris.split(",") # Kita ubah barisnya agar tanda koma (,) yang ada di baris hilang
                stok_dict[KodeBarang] = {"nama": NamaBarang, "stok": int(Stok)} # Kita definisikan setiap key memiliki value berdasarkan Kode Barang
        
    except FileNotFoundError: # Di eksekusi kalau file tidak ada
        print("File belum ada. Memulai dengan data kosong")
    return stok_dict # Kita mengembalikan stok_dict
# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict): # Kita membuat fungsi simpan_stok()
    # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
    # Hint: with open(nama_file, "w", encoding="utf-8") as f:
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    with open(nama_file, "w", encoding="utf-8") as f: # Kita membuka dan menimpa file
       for kode in sorted(stok_dict.keys()): # Ambil semua kode (key) barang dan diurutkan
           nama = stok_dict[kode]["nama"] # Ambil nama dari dictionary
           stok = stok_dict[kode]["stok"] # Ambil stok dari dictionary
           f.write(f"{kode}, {nama},{stok}\n") # Menulis kode, nama, stok di file

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    # TODO: Jika kosong, tampilkan pesan stok kosong
    # TODO: Tampilkan dengan format rapi: kode | nama | stok
    if not stok_dict: # Jika tidak ditemukan barang maka outputnya adalah barangnya kosong
        print("\nStok barang kosong")
        return
    print("\n=== Daftar Barang ===")
    print(f"{'kode':<10} | {'nama':<15} | {'stok':>5}")
    """
    untuk tampilan yang rapi, atur lebar kolom
    {'kode' :<10} artinya kode rata kiri dengan lebar kolom 10 karakter
    {'nama' :<15} artinya nama rata kiri dengan lebar kolom 15 karakter
    {'stok' :>5} artinya stok rata kanan dengan lebar kolom 5 
    """
    print("-"*30)

    for kode in sorted(stok_dict.keys()): # Ambil semua kode (key) barang dan diurutkan
        nama = stok_dict[kode]["nama"] # Ambil nama dari dictionary
        stok = stok_dict[kode]["stok"] # Ambil stok dari dictionary
        print(f"{kode:<10} | {nama:<15} | {stok:>5}") # Menulis kode, nama, dan stok yang sudah diratakan sesuai angkaa dan simbol di file 
# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip() # Masukkan kode barang di fungsi input
    # TODO: Cek apakah kode ada di dictionary
    # Jika ada: tampilkan detail barang
    # Jika tidak ada: tampilkan 'Barang tidak ditemukan'
    if kode in stok_dict:
        print("\n=== Barang Ditemukan ===")
        print(f"Kode  : {kode}")
        print(f"Nama  : {stok_dict[kode]['nama']}")
        print(f"Stok  : {stok_dict[kode]['stok']}")
    else:
        print(f"\nBarang dengan kode '{kode}' tidak ditemukan.")

    """
    Mengecek jika ada barang di filenya.

    Jika ada nanti akan ditampilkan kode, nama, 
    dan stok.

    Jika tidak ada maka akan menampilkan ketiadaan kode tersebut 
    """

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    # TODO: Validasi kode tidak boleh duplikat
    # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
    # TODO: Input stok awal (integer)
    # Hint: stok_awal = int(input(...))
    # TODO: Simpan ke dictionary

    kode = input("Masukkan kode barang baru: ").strip() # Masukkan kode barang yang baru
    if kode in stok_dict:
        print(f"Gagal: Kode '{kode}' sudah digunakan oleh {stok_dict[kode]['nama']}.")
        return # Mengecek apakah barang yang dicari ada di file atau tidak 
    nama = input("Masukkan nama barang: ").strip() # Masukkan nama barang yang baru
    try:
        stok_awal = int(input("Masukkan stok awal: ").strip()) # Memasukkan stok awal yang baru
        stok_dict[kode] = {"nama": nama, "stok": stok_awal} # Mengupdate stok awal
        print("Barang berhasil ditambahkan.")
    except ValueError:
        print("Error: Stok harus berupa angka.") # Jika input yang dimasukkan bukan berupa angka
    
# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip() # Memasukkan kode barang yang ingin di update

    # TODO: Cek apakah kode ada di dictionary
    # Jika tidak ada: tampilkan pesan dan return
    if kode not in stok_dict: # Mengecek apakah barang yang dicari ada di file atau tidak
        print("Barang tidak ditemukan.")
        return
    
    print("Pilih jenis update:") 
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    # Pilih jenis update (Tambah stok/Kurangi stok)

    try:
        jumlah = int(input("Masukkan jumlah: ").strip()) # Masukkan jumlah yang ingin ditambah/dikurang
        
        stok_sekarang = stok_dict[kode]["stok"] 
        stok_baru = stok_sekarang # Mendefinisikan stok sekarang dengan stok baru
        
        # TODO: Logika update
        if pilihan == "1":
            # - Jika pilihan 1: stok = stok + jumlah
            stok_baru = stok_sekarang + jumlah
        elif pilihan == "2":
            # - Jika pilihan 2: stok = stok - jumlah
            stok_baru = stok_sekarang - jumlah
        else:
            print("Pilihan tidak valid.") # Jika input yang dimasukkan bukan 1 atau 2
            return
            
        # - Jika hasil < 0: batalkan dan tampilkan error
        if stok_baru < 0:
            print("Gagal: Stok tidak boleh negatif.")
        else:
            stok_dict[kode]["stok"] = stok_baru # Mendefinisikan stok sekarang dengan stok baru
            print(f"Berhasil update. Stok sekarang: {stok_baru}")
            
    except ValueError:
        print("Error: Input jumlah harus angka.") # Jika input yang dimasukkan bukan berupa angka

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        # Menampilkan beberapa pilihan di menu yang bisa dipilih sesuai angka
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_semua(stok_barang) # Menampilkan stok barang
        elif pilihan == "2":
            cari_barang(stok_barang) # Mencari barang yang ada di stok barang
        elif pilihan == "3":
            tambah_barang(stok_barang) # Menambah barang
        elif pilihan == "4":
            update_stok(stok_barang) # Menambah/Mengurangi jumlah stok yang ada
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang) # Menyimpan informasi terbaru mengenai barang dan jumlah stok
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.") # Program selesai
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.") # Pilihan yang tidak valid

# Menjalankan program utama
if __name__ == "__main__":
    main()