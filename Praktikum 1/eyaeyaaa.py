# ===============================================================
# Praktikum 1 : Konsep ADT dan file Handling
# Latihan Dasar 1 : Membaca seluruh isi file data
# ===============================================================
print("== Membuka file dalam satu string ==")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
     filee = file.read()
     print(filee)

print("Tipe data:", type(filee))

print("== Membuka file per baris ==")

jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
     for baris in file:
          jumlah_baris += 1
          baris = baris.strip()
          print("Baris ke", jumlah_baris)
          print(baris)
     
# ===============================================================
# Praktikum 1 : Konsep ADT dan file Handling
# Latihan Dasar 2 : Parsing data
# ===============================================================
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
     for baris in file:
          baris = baris.strip()
          nim, nama, nilai = baris.split(",")
          print(f"nama: {nama} | nilai: {nilai} | nim: {nim}")
        
# ===============================================================
# Praktikum 1 : Konsep ADT dan file Handling
# Latihan Dasar 3 : Membaca Data dan Menyimpannya ke struktur Data List
# ===============================================================
data_list = []
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
     for baris in file:
          baris = baris.strip()
          nim, nama, nilai = baris.split(",")
          data_list.append((nim,nama,int(nilai)))

     
print("=== Menampilkan list ===")
print(data_list)
print("Contoh record ke 1:", data_list[0])
print("Contoh record ke 2:", data_list[1])
print("Jumlah_record =", len(data_list))
     
# ===============================================================
# Praktikum 1 : Konsep ADT dan file Handling
# Latihan Dasar 4 : Membaca Data dan Menyimpannya ke Structur Dictionary
# ===============================================================

data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_dict[nim] = {
           "nama": nama,
           "nilai": int(nilai)
        }

print("=== Menampilkan Data Dictionary ===")
print(data_dict)
          