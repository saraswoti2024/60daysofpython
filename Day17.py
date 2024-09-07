class user:
   def __init__(self,id,name) -> None:
      self.id=id
      self.name = name
      self.followers = 0
      self.following = 0

   def follow(self,user):
      user.followers+=1
      self.following+=1

user_1 = user(5,"saraswoti")
user_2 = user(12,"Angela")

print(user_1.id,user_1.name,user_1.followers)
print(user_2.id,user_2.name,user_2.followers)

user_1.follow(user_2) 
print(user_1.followers) 
print(user_1.following) #following ma self xa , means aafno tahi object ko which is user1
print(user_2.followers) #followers ma user xa user means follow(vitrw)
print(user_2.following)
##----------quiz project---------------






