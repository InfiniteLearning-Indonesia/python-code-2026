my_list = [10, 20, 30, 40, 50]

# append(): Menambahkan elemen ke akhir daftar
my_list.append(60)
print("Setelah append:", my_list)  # Output: [10, 20, 30, 40, 50, 60]

# clear(): Menghapus semua elemen dari daftar
copy_list = my_list.copy()  # Salin daftar sebelum dihapus
my_list.clear()
print("Setelah clear:", my_list)  # Output: []

# copy(): Membuat salinan daftar
print("Salinan daftar:", copy_list)  # Output: [10, 20, 30, 40, 50, 60]

# count(): Menghitung jumlah elemen dengan nilai tertentu
count_20 = copy_list.count(20)
print("Jumlah elemen '20':", count_20)  # Output: 1

# extend(): Menambahkan elemen dari daftar lain
copy_list.extend([70, 80])
print("Setelah extend:", copy_list)  # Output: [10, 20, 30, 40, 50, 60, 70, 80]

# index(): Mendapatkan indeks elemen pertama dengan nilai tertentu
index_40 = copy_list.index(40)
print("Indeks elemen '40':", index_40)  # Output: 3

# insert(): Menambahkan elemen di posisi tertentu
copy_list.insert(2, 25)
print("Setelah insert:", copy_list)  # Output: [10, 20, 25, 30, 40, 50, 60, 70, 80]

# pop(): Menghapus elemen di posisi tertentu
removed_element = copy_list.pop(2)
print("Elemen yang dihapus:", removed_element)  # Output: 25
print("Setelah pop:", copy_list)  # Output: [10, 20, 30, 40, 50, 60, 70, 80]

# remove(): Menghapus elemen pertama dengan nilai tertentu
copy_list.remove(50)
print("Setelah remove:", copy_list)  # Output: [10, 20, 30, 40, 60, 70, 80]

# reverse(): Membalik urutan elemen
copy_list.reverse()
print("Setelah reverse:", copy_list)  # Output: [80, 70, 60, 40, 30, 20, 10]

# sort(): Mengurutkan elemen
copy_list.sort()
print("Setelah sort:", copy_list)  # Output: [10, 20, 30, 40, 60, 70, 80]
