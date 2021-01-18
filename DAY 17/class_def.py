# class User:
#     def __init__(self):
#         print("new user being created..")
#
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Selva"
#
# print(f"The id is {user_1.id} and the name is {user_1.username}")
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Ganesh"
#
# print(f"The id is {user_2.id} and the name is {user_2.username}")

"""Updated Code which has attributes for the class"""


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0


user = User("001", "Selva")
print(user.follower)
