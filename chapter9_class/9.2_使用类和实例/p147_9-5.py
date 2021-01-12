class User():
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
        self.login_attempts = 0
    def describe_user(self):
        print('Your first name is ' + self.first.title())
        print('Your last name is ' + self.last.title())

    def greet_user(self):
        print('Hello! ' + self.first.title() + ' ' + self.last.title())

    def increment_login_attempts(self, num=1):
        self.login_attempts += num

    def reset_login_attempts(self):
        self.login_attempts = 0


my_user = User('zhang', 'chen')
my_user.greet_user()
my_user.describe_user()

user = User('zhang', 'wei')
user.greet_user()
user.describe_user()

test_user = User('zhao', 'yang')
test_user.increment_login_attempts()
print(test_user.login_attempts)
test_user.increment_login_attempts()
print(test_user.login_attempts)
test_user.increment_login_attempts()
print(test_user.login_attempts)
test_user.increment_login_attempts()
print(test_user.login_attempts)
test_user.reset_login_attempts()
print(test_user.login_attempts)