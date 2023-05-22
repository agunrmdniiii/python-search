def binary_search(dictionary, word):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2
        entry = dictionary[mid]

        if entry[0] == word:
            return entry[1]
        elif entry[0] < word:
            left = mid + 1
        else:
            right = mid - 1

    return "Kata tidak ditemukan dalam kamus ajaib."

# Kamus ajaib
dictionary = [
    ("Apple", "Buah Apel"),
    ("Banana", "Buah Pisang"),
    ("Cat", "Kucing"),
    ("Duck", "Bebek"),
    ("Elephant", "Gajah")
]

# Meminta input kata yang ingin dicari definisinya
word = input("Masukkan kata yang ingin Anda cari definisinya: ")

# Mencari definisi kata menggunakan binary search
definition = binary_search(dictionary, word)

# Menampilkan hasil
print("Definisi kata", word, "adalah:", definition)
