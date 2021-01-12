class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('restaurant_name: \n - ' + self.restaurant_name)
        print('cuisine_type: \n - ' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open')


my_restaurant = Restaurant('老八', '汉堡店')
nine_restaurant = Restaurant('老九', '柠檬店')
ten_restaurant = Restaurant('老十', '腐乳店')

my_restaurant.describe_restaurant()
nine_restaurant.describe_restaurant()
ten_restaurant.describe_restaurant()


