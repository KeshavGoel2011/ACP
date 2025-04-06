#age counter
try:
    age = int(input("Enter your age: "))
    if type(age) is int:
        if age%2==0:
            print("Your age is even")
        elif age%2==1:
            print ("Your age is odd")
        else:
            print("Your age is zero")
    else:
        raise ValueError

except ValueError as ve:
    print("Exception", ve)