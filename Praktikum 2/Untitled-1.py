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

if __name__ == "__name__":
    main()