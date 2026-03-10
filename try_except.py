try:
    hasil = 10 / 2
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan 0!")
else:
    print("Hasil:", hasil)
finally:
    print("Operasi selesai.")