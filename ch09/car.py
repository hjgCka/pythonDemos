"""一个用来表示汽车的类"""

class Car:
    """模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"this car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """更新里程表读数为指定的值"""
        self.odometer_reading = mileage

    def increase_odometer(self, miles):
        self.odometer_reading += miles

#my_new_car = Car('audi', 'a4', 2024)
#print(my_new_car.get_descriptive_name())

#my_new_car.odometer_reading = 100
#my_new_car.update_odometer(90)
#my_new_car.increase_odometer(50)
#my_new_car.read_odometer()

class Battery:
    """模拟电动汽车的电池"""
    def __init__(self, battery_size=50):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size} kWh battery.")

    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        range = 0
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 60:
            range = 180

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()