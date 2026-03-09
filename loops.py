# This is not a loop, this is string multiplication 
print("Saya berjanji untuk tidak mengulangi perbuatan tersebut \n" * 5)

for i in range(10):
    if i == 5:
        print("Tapi boong")
    print("Saya berjanji untuk tidak mengulangi perbuatan tersebut")

# Seakan mendeklarasikan variabel i tapi 10x sesuai range(10)

fruits = ["apple", "banana", "cherry"] # List of Fruits

for fruit in fruits:
    print(fruit)

# While Loop
password = "2026"

while password != "2026":
    password = input("Enter password: ")
print("Access granted!")