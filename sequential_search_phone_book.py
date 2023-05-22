def sequential_search(nama, daftar_nama, daftar_nomor):
    for i in range(len(daftar_nama)):
        if daftar_nama[i] == nama:
            return daftar_nomor[i]
    return None

# Daftar nama dan nomor telepon
daftar_nama = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Davis"]
daftar_nomor = ["081234567890", "089876543210", "087811223344", "082122232425"]

# Nama yang ingin dicari nomor teleponnya
nama_cari = "Jane Smith"

# Mencari nomor telepon menggunakan sequential search
nomor_telepon = sequential_search(nama_cari, daftar_nama, daftar_nomor)

# Menampilkan hasil
if nomor_telepon:
    print("Nomor telepon", nama_cari, "adalah:", nomor_telepon)
else:
    print("Nomor telepon", nama_cari, "tidak ditemukan.")
