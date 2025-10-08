class User:
    """创建一个名为User的类"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"login_attempts = {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Reset login_attempts ;login_attempts = {self.login_attempts}")

new_user = User("Lee", 'ZF')
new_user.describe_user()
new_user.greet_user()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

new_user.reset_login_attempts()

