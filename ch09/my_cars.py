#from car import Car, ElectricCar

import car

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_model3 = car.ElectricCar('tesla', 'model3', 2024)
print(my_model3.get_descriptive_name())