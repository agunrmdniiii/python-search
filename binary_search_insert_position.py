def binary_search_insertion_index(data, target):
    left = 0
    right = len(data) - 1
    insertion_index = len(data)  # Default: sisipkan di akhir daftar

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            # Elemen sudah ada dalam daftar
            return mid

        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            insertion_index = mid

    # Elemen tidak ada dalam daftar, mengembalikan indeks sisipan
    return insertion_index

# Daftar data yang sudah diurutkan secara menaik
data = [2, 4, 6, 8, 10, 12, 14]

# Elemen target
target = 7

# Mencari posisi sisipan menggunakan binary search
sisipan_indeks = binary_search_insertion_index(data, target)

# Menampilkan hasil
if sisipan_indeks == len(data):
    print("Elemen", target, "dapat disisipkan pada indeks", sisipan_indeks, "untuk menjaga daftar tetap terurut.")
else:
    print("Elemen", target, "sudah ada dalam daftar pada indeks", sisipan_indeks, ".")
