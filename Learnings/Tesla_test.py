
age = input("What is your age?: ")
	
##default will be zero
def  checkDriverAge(age='0'):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
		
print(checkDriverAge(age))
print(checkDriverAge())
print(checkDriverAge(age='9'))