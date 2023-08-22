import random
lower="abcdefghijklmnopqrstuvwxyz"
upper=lower.upper()
num="1234567890"
symbols="!@#$%^&*_=+-{}|\;:<>?/.,"
all=lower+upper+num+symbols
while 1:
    password_len=int(input("length of the password: "))
    password_count=int(input("How many passwords: "))
    for i in range(0,password_count):
        password=''
        for i in range(0,password_len):
            password_char="".join(random.choice(all))
            password=password+password_char
        print("your password: ",password)