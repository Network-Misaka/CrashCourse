class Car:
    # 一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        # 打印一条指出汽车里程的消息
        msg = "这破车已经走了 " + str(self.odometer_reading) + " 公里了哦"
        return msg

    def update_odometer(self, mileage):
        # 将里程表读数设置为指定的值
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('耍小聪明，不行！')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
my_new_car.odometer_reading = 24  # 直接修改属性的值
print(my_new_car.read_odometer())
my_new_car.update_odometer(30)    # 通过方法修改属性的值
print(my_new_car.read_odometer())
my_new_car.update_odometer(28)
print(my_new_car.read_odometer())
my_new_car.update_odometer(38)
print(my_new_car.read_odometer())
my_new_car.increment_odometer(100)
print(my_new_car.read_odometer())


