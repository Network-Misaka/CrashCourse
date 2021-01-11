def make_pizza(size, *toppings):
    # 打印顾客点的所有配料
    # **代表字典 *代表元组
    print('\n Making a ' + str(size) + '-inch pizza ' +
          'with the followings toppings')
    for topping in toppings:
        print('- ' + topping + '\t')


make_pizza('14', 'salt', 'butter', 'cheese')
# make_pizza('salt', 'butter', 'cheese', size='14') 这个不行
# 按顺序来，第一个不变
# 形参 *toppings 创建了一个元组，接收传进来的实参
