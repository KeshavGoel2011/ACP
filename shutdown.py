#shutdown your pc
import os
stdown= input("Do you want to shutdown your system (yes/no): ")
def shutdown():
    if stdown == "no":
      exit()
    else:
        secs = int(input("Enter in how many seconds you want to shut down your system: "))
        os.system(f'shutdown /s /t {secs}')
        return (f"Your System is going to shutdown in {secs}")

print(shutdown())