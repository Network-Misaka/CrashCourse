class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('restaurant_name: \n - ' + self.restaurant_name)
        print('cuisine_type: \n - ' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open')

    def set_number_severed(self, num):
        self.number_served = num

    def increment_number_severed(self, nums):
        self.number_served += nums


class RestaurantIceCream(Restaurant):
    def __init__(self, flavors):
        super.__init__(flavors)
        self.flavors = flavors

        def show_flavors():
            for flavor in flavors:
                print(flavor)


flavors_list = ['chocolate', 'berry', 'pineapple', 'apple']
ice_cream = RestaurantIceCream(flavors=flavors_list)
ice_cream.show_flavors()

