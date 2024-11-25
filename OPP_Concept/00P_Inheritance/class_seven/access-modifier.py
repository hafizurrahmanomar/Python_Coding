class User:
    def __init__(self, name, email, phone, password):
        self.name = name # public
        self.email = email # public
        self._phone = phone # protected
        self.__password = password # private
    
    def __secret_method(self): # private
        pass
    
    def save_password_to_db(self):
        print(self.__password)
        self.__secret_method()
    
    def get_password(self):
        return self.__password
    
    def set_password(self, new_password):
        self.__password = new_password

    def __secret_method(self):
        pass


user1 = User("Sakib", "sakib123@gmail.com", "1234", "!@#$ASDF1234")

print(user1.name)
print(user1.email)
# print(user1.phone)

user1.name = "Tamim"

print(user1.get_password())
user1.set_password("ASLKDJALSKD")
print(user1.get_password())

user1.__secret_method()
# user1.save_password_to_db()