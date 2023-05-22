def binary_search_definition(kata, kamus):
    left = 0
    right = len(kamus) - 1

    while left <= right:
        mid = (left + right) // 2

        if kamus[mid][0] == kata:
            # Kata ditemukan dalam kamus, mengembalikan definisi
            return kamus[mid][1]

        if kamus[mid][0] < kata:
            left = mid + 1
        else:
            right = mid - 1

    # Kata tidak ditemukan dalam kamus
    return None

# Kamus ajaib
kamus = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

# Kata yang ingin dicari definisinya
kata_cari = "Banana"

# Mencari definisi kata menggunakan binary search
definisi = binary_search_definition(kata_cari, kamus)

# Menampilkan hasil
if definisi:
    print("Definisi dari kata", kata_cari, "adalah:", definisi)
else:
    print("Kata", kata_cari, "tidak ditemukan dalam kamus.")
