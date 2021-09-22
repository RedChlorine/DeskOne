import pytemperature

converted = None

print("This is a Kelvin Calculator!")
try:
    temperature = float(input("What is the temperature? "))
except ValueError:
    temperature = 0

while not converted:
    unit = input("(C)elcius? or (F)arenheit? ")

    if unit.upper() == "C":
        converted = pytemperature.c2k(temperature)
    elif unit.upper() == "F":
        converted = pytemperature.f2k(temperature)
    else:
        converted = None

print(f"{converted}K is the result")
print("There ya go!")
