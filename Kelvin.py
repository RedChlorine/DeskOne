print("This is a Kelvin Calculator!")
temperature = float(input("What is the temperature? "))
unit = input("(C)elcius? or (F)arenheit? ")
converted = float(temperature+273.6)

if unit.upper() == "C":
   print(str(converted)+"K is the result")
elif unit.upper() =="F":
   print(str((converted-305)*5/9+273) +"K is the result")
print("There ya go!")

