# Concatenation
nama_depan = "Messal"
nama_belakang = "Veronica"

print(nama_depan + " " + nama_belakang) # Menggabungkan string dengan operator +
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap) # Menampilkan isi variabel nama_lengkap

# Repetition
print("ha \n" * 5)
print("ha" * 5)

# Slicing
nama = "Messal Veronica" # Nama formal
x = "Hello"
print(nama[0]) # Mengakses karakter pertama (M)
print(x[1:4]) # Mengakses karakter dari indeks 1 hingga 3
# [H, e, l, l, o] 
# [0, 1, 2, 3, 4]
# [1:4] indeks 1 sampai sebelum 4

# Length
print(len(nama))
# [M, e, s, s, a, l, , V, e, r, o, n, i, c, a]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Uppercase dan Lowercase
print(nama.upper()) # Mengubah semua karakter menjadi huruf besar/kapital
print(nama.lower()) # Mengubah semua karakter menjadi huruf kecil

# Strip
contoh = " Muhammad Sirojul Fuad  "
print(contoh.strip()) # Menghapus spasi di awal dan akhir string

# Replace
name = "Jojon"
print(name.replace("o", "a")) # Mengganti karakter 'a' dengan 'o' dalam string name

# Split
kalimat = "Republik Indonesia"
print(kalimat.split())

# Join
kata_kata = ["Republik", "Indonesia"]
print(" ".join(kata_kata)) # Menggabungkan elemen-elemen dalam list kata_kata menjadi sebuah string dengan spasi sebagai pemisah