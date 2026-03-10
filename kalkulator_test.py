# Import seluruh modul
import kalkulator 

print(kalkulator.tambah(10, 5))             # 15
print(kalkulator.PI)                                  # 3.14159
print(kalkulator.luas_lingkaran(7))       # 153.93791

# Import fungsi tertentu
from kalkulator import tambah, kurang, PI

print(tambah(20, 30))                              # 50
print(PI)                                                      # 3.14159

# Import dengan alias
import kalkulator as calc

print(calc.kali(6, 7))                                     # 42