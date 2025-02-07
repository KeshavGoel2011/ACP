#ASCII value checker
char = input("Enter a charcter: ")
if len(char) == 1:
   ascii_value = ord(char)
   print(f"The ASCII value of {char} is {ascii_value} ")
else:
   print("please enter only one character")