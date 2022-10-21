print ("\n Have a nice day!")
from datetime import date

name = input("\n Please enter your name: ")
print (" Nice to meet you " + name + '!\n')

def age(yearborn):
    return date.today().year - yearborn
    
yearborn = int(input(" Please enter your birth year: "))

print(f"\n Whoa, you are {age (yearborn)} years old!")
