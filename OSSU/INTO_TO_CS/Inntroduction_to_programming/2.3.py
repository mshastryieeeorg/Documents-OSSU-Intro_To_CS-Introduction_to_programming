import decimal
hours = input("Enter Hours:")
rate = input("Enter Rate:")
#print(type(hours))
#print(type(rate))
fhours = float(hours)
frate = float(rate)
#print(type(fhours))
#print(type(frate))
frate = fhours*frate
sfrate = str(frate)
print("Pay:" + sfrate)
