import random 
given=random.randint(000000,100000)
user_name=input("enter the name: ")
print("hi",user_name)
print("here is your otp:",given)
password=input("enter the otp to login:")
if password==str(given):
    print("login success")
else:
    password!=str(given)
    print("login failed")
