# Exercise 1-1
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def decribe_restaurant(self):
#         print(f"Restaurant Name: {self.restaurant_name}")
#         print(f"Cuisine Type: {self.cuisine_type}")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is now open for business!")

# restaurant = Restaurant("The Good Food Place", "Italian")

# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant.decribe_restaurant()
# restaurant.open_restaurant()


# Exercise 1-2
# restaurant1= Restaurant("Restaurant1","VietNam")
# print(restaurant1.restaurant_name)
# print(restaurant1.cuisine_type)
# restaurant1.open_restaurant

# restaurant2= Restaurant("Restaurant2","Chinese")
# print(restaurant2.restaurant_name)
# print(restaurant2.cuisine_type)
# restaurant2.open_restaurant

# restaurant3= Restaurant("Restaurant3","Thailand")
# print(restaurant3.restaurant_name)
# print(restaurant3.cuisine_type)
# restaurant3.open_restaurant

# Exercise 1-3
# class User():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def decribe_user(self):
#         print(f"First Name: {self.first_name}")
#         print(f"Last Name: {self.last_name}")
#     def greet_user(self):
#         print(f"Greeting {self.first_name} {self.last_name} go to system")

# user1 = User("Nguyen", "Dung")
# print(user1.first_name)
# print(user1.last_name)
# user1.decribe_user()
# user1.greet_user()

# Exercise 1-4:
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type,number_served):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served=0

#     def decribe_restaurant(self):
#         print(f"Restaurant Name: {self.restaurant_name}")
#         print(f"Cuisine Type: {self.cuisine_type}")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is now open for business!")
    
#     def set_number_served(self,number):
#         self.number_served = number
        
#     def increment_served(self,number):
#         self.number_served+=number

# restaurant=Restaurant("Michilin","Italia",0)

# print(f"Number of customers served: {restaurant.number_served}")

# restaurant.number_served = 5
# print(f"Number of customers served after update: {restaurant.number_served}")

# Exercise 1-5
# class User():
#     def __init__(self, first_name, last_name,login_attemps):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attemps=0

#     def decribe_user(self):
#         print(f"First Name: {self.first_name}")
#         print(f"Last Name: {self.last_name}")

#     def greet_user(self):
#         print(f"Greeting {self.first_name} {self.last_name} go to system")

#     def increment_login_attemps(self):
#         self.login_attemps += 1
    
#     def reset_login_attemps(self):
#         self.login_attemps=0

# user1=User("Nguyen","Dung",0)
# print(f"Number of login attemps: {user1.login_attemps}")
# user1.increment_login_attemps()
# user1.increment_login_attemps()
# user1.increment_login_attemps()
# print(f"increment_login_attemps:{user1.login_attemps}")
# user1.reset_login_attemps()
# print(f"increment_login_attemps:{user1.login_attemps}")




