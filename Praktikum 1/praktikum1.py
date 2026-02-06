# ===============================================================
# Praktikum 1 : Konsep ADT dan file Handling
# Latihan Dasar 1 : Membaca seluruh isi file data
# ===============================================================

# Membuka file dalam mode read ("r")
print("=====Membuka file dalam satu string======")
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file: #mengambil data dan menyimpan semua di variabel
    isi_file = file.read()
print(isi_file)

print("Tipe Data :", type(isi_file))

#membuka file per baris
print("=====Membuka file per baris=====")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("Baris ke- ", jumlah_baris)
        print("isinya :", baris)


# ===============================================================
# Praktikum 1 : Konsep ADT dan file Handling
# Latihan Dasar 2 : Parsing data
# ===============================================================

# Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data 
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilang karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai) #menampilkan data dalam satuan bentuk  kolom
        
# ===============================================================
# Praktikum 1 : Konsep ADT dan file Handling
# Latihan Dasar 3 : Membaca Data dan Menyimpannya ke struktur Data List
# ===============================================================

data_list = [] #inisialisasi list untuk menampung data

with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilang karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim,nama,int(nilai)]) #menyimpan data ke list
print("===== Menampilkan List=====")
print(data_list)
print("Contoh record ke 1", data_list[0])
print("Contoh record ke 2", data_list[1])

print("Jumlah Record", len(data_list))

# ===============================================================
# Praktikum 1 : Konsep ADT dan file Handling
# Latihan Dasar 4 : Membaca Data dan Menyimpannya ke Structur Dictionary
# ===============================================================

data_dict = {} #inisialisasi dictionary

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilang karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        #simpan data dalam dictionary {key, value}
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("=== Menampilkan Data Dictionary====")
print(data_dict)