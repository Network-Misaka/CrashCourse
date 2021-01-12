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


class Battery:
    # 一次模拟电动汽车电瓶的简单尝试
    def __init__(self, battery_size=70):
        # 初始化电瓶的属性
        self.battery_size = battery_size

    def battery_info(self):
        # 打印一条描述电瓶容量的消息
        print("This car has a " + str(self.battery_size) + "-kWh battery")


class ElectricCar(Car):
    # 电动汽车的独特之处
    def __init__(self, make, model, year):
        # 初始化父类的属性
        super().__init__(make, model, year)
    #     self.battery_size = 70
    #
    # def battery_info(self):
    #     print("This car ha a " + str(self.battery_size) + '-kWh battery')
        self.battery = Battery()


tesla = ElectricCar('tesla', 'model s', '2016')
print(tesla.get_descriptive_name())
tesla.battery.battery_info()