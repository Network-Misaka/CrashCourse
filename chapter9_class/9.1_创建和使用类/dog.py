class Dog():
    # 一次模拟小狗的简单尝试
    def __init__(self, name, age):
        # 初始化属性name和age
        self.name = name
        self.age = age

    def sit(self):
        # 模拟小狗被命令时蹲下
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        # 模拟小狗被命令时打滚
        print(self.name.title() + ' rolled over! ')


# 实例化类
my_dog = Dog('nono', 5)


# 调用实例化的类
print("my dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old")

# 调用实例化类的方法

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('bark', 5)
your_dog.roll_over()
your_dog.sit()