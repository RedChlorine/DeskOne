print("Hello World!!!")

#print and operators
print("OwO") #strings = str. they are always in ""
print("//" * 10) #str followed by opperator

#Variables
price = 50 #identifyer
print("R" + str(price)) #str()is a modifier or converter
print("//"*10)


#The age app
print("Hi therer! I will tell you your birth year.")
print("/////"*10)
currentYear = input("What is the current year? ")
theirAge = input("How old are you?" )
birthYear = int(currentYear) - int(theirAge) #modified the input str to integers = int()
print("You were born in " + str(birthYear)+ "!")