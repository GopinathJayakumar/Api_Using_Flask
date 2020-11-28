import random

otp = random.randrange(100000, 1000000)
print(otp)

user_input = int(input("Enter the OTP: "))
if user_input == otp:
    print("Access Granted")
else:
    print("Access Denied!!!")