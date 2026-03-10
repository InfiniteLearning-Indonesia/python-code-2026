PI = 3.14159

def tambah(a, b):
    """Menjumlahkan dua angka"""
    return a + b

def kurang(a, b):
    """Mengurangkan dua angka"""
    return a - b

def kali(a, b):
    """Mengalikan dua angka"""
    return a * b

def bagi(a, b):
 """Membagi dua angka"""
 if b == 0:
    raise ValueError("Tidak bisa membagi dengan 0!")
 return a / b

def pangkat(a, n=2):
 """Memangkatkan angka"""
 return a ** n

def luas_lingkaran(r):
 """Menghitung luas lingkaran"""
 return PI * r ** 2