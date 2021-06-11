class User:
    def __init__(self, user_id): #constructor
        self.id = user_id
        self.followers = 0 #defualt value
        self.following = 0

    def follow(self, user): #add method
        self.following += 1
        user.followers += 1

user_1 = User("001", "Angela")
user_2 = User("002","Wpaw")

user_1.follow(user_2)

user_1.sad = 'kun' #add atributes



