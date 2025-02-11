#To check if someone is between 10-20 years old
age = int(input("Enter your age: "))

if 10 <= age <= 20 :
    print("You are eligible to join Raj's class")
    if age <= 15:
        print("You are also eligible to compete in class kids'competition")
    if age > 15:
        print("You are also eligible to join the football team")
        if age >= 18:
            print("You are also eligible to vote in elections")
else:
    print("You are not eligible to join Raj's class")
