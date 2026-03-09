class Car:
  def __init__(self, brand, model, year=2021):
    self.brand = brand
    self.model = model
    self.year = year

car1 = Car("Mazda", "CX-5")
car2 = Car("Ford", "Mustang", 1967)

print(car1.model)
print(car1.year)
print(car1.brand)
