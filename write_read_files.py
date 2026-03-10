# Menambah tulisan baru
with open('file.txt', 'w') as file: # 'a' untuk append mode (menambahkan tanpa menghapus isi sebelumnya)
  file.write("\nHari ini hari Selasa!")

# Membuka file dalam mode read
with open('file.txt', 'r') as file: # 'r' untuk read mode
  content = file.read() # Membaca seluruh isi file
  print(content)    # Menampilkan isi file

# # Menulis sesuatu yang baru ke file
# with open('file.txt', 'w') as file: # 'w' untuk write mode (menghapus isi file sebelumnya)
#   file.write("Ini adalah tulisan baru cuy\n")
#   file.write("Ini juga")

