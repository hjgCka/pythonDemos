from car import ElectricCar

my_model3 = ElectricCar('tesla', 'model3', 2024)
print(my_model3.get_descriptive_name())
my_model3.battery.describe_battery()
my_model3.battery.get_range()