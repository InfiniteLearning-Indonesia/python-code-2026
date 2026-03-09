# List
B=["Infinite", 2026, "Learning", True, 87.1] # List pertama kita yang berisi 3 buah char/string.

print(B[1:]) # Mengakses elemen mulai dari indeks 1 hingga akhir list (termasuk indeks 1)
print(B[:1]) # Mengakses elemen sebelum indeks 1 (tidak termasuk indeks 1)

# Tuple
A=(12.1,"Infinite",False, 89,"Learning")

print(A[3]) # Mengakses elemen ke-3 (indeks 3) dari tuple A
print(A[-1]) # Mengakses elemen terakhir dari tuple A

# Sets
X = {'A', 'B', 'C', 'D'}
Y = {'A', 'C', 'D', 'E', 'Z'}
print(X.union(Y))

# Dictionary
student = {
"name": "Arifian", # Key and Value
"age": 24, # int
"major": "Computer Science", # str
"is_graduated": True, # bool
"height": 165.5 # float
}

print(student)

