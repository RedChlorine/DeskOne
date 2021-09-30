#Decimals##################
import decimal
from decimal import Decimal
borderLine = "///"*10


taxRate = Decimal('7.25')/Decimal(100)
purchaseAmount = Decimal('2.95')
penny = Decimal('0.01')
totalAmount = purchaseAmount+taxRate*purchaseAmount

totalAmount.quantize(penny, decimal.ROUND_UP)

print(totalAmount)
print(borderLine)

##################Fractions###################
from fractions import Fraction

sugarCups = Fraction('2.5')
scalingFactor = Fraction(5/8)

print(sugarCups*scalingFactor) #the output is in fraction form n/d
print(borderLine)

#############################Simplification via Fraction()##############
print(Fraction(24/16)) #output is simplified
print(borderLine)

###############################Floating Point Approximations############
answer = (55/7)*(7/55)
print (str(answer)+" float approximation")
print ("--> "+str(round(answer, 3))+" rounded approximation, to 3 decimal places")
print(borderLine)

################################f-strings###############################
#first declair the array you want in the f-string
id = "IAD"
minTemp = 20
maxTemp = 28
location = "Dallas International Airport"
precipitation = 0.6

print(f' {id} : {location} : {minTemp} / {maxTemp} / {precipitation})')
print (borderLine)

##############adding optional data to as f-string#######################
id = "IAD"
minTemp = 20
maxTemp = 28
location = "Dallas International Airport"
precipitation = 0.6

print(f' {id:s} : {location:s} : {minTemp:d} / {maxTemp:d} / {precipitation:f})')
print (borderLine)

############Adding lengths to f-strings##################################
id = "IAD"
minTemp = 20
maxTemp = 28
location = "Dallas International Airport"
precipitation = 0.6

print(f' {id:s} : {location:19s} : {minTemp:3d} / {maxTemp:3d} / {precipitation:5.2f})')
print (borderLine)
