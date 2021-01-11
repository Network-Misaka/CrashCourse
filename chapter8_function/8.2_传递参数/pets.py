# def describe_pet(animal_type, pet_name):
def describe_pet(animal_type, pet_name='dog'):
    # 显示宠物的信息
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name + '.')


describe_pet('teddy','nono')
describe_pet('traditional','xiaohu')

describe_pet(pet_name='niuniu',animal_type='dick')
describe_pet(animal_type='willow')