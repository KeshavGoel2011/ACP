# program to check alphabets
char = str(input("Enter an alphabet: "))

if "A" <= char <= "Z" or "a" <= char <= "z":
  print(char, "is an alphabet")
else:
  print(char, "is not an alphabet")