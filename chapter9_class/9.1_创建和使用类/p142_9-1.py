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

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()