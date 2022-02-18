def electricCalc(amused,nf):
    return((amused*0.95)/nf)

def vehicleCalc(distance,mil,nf,type):
    if type.lower()=="p":
        return(((distance/mil)*2.392)/nf)
    else:
        return(((distance/mil)*2.640)/nf)      

def flightCalc(inthours,dmhours):
    total = 0
    total+=((dmhours*90)/75)
    total+=((inthours*90)/416)
    return(total/365)

def iceCalc(carbon):
    return(carbon*650)

################################################################################################################################################################################################

total = 0
# electric calc

s = str(input("Enter your name : "))
nf = int(input("Enter number of family members : "))
print("Now lets calculate your carbon footprint")

eunit = int(input("How much unit of electricity has used in your home till now ? : "))
print("Your electric carbon footprint is : ",electricCalc(eunit,nf),"kg of CO2")
total+=electricCalc(eunit,nf)
print()

# vehicle calc 

vno = int(input("How many vehicles you have? : "))
carbon = 0
for i in range(1,vno+1):
    print("Enter detail about vehicle ",i)
    vtype = str(input("What type of vehicle is it ? Petrol / Diesel ? ( p/d ) : "))
    mil = int(input("What is its mileage ? ( kms/liter ) : "))
    dis = int(input("Total distance covered by that vehicle ? : "))
    carbon+=vehicleCalc(dis,mil,nf,vtype)
print("Your vehicle carbon footprint is : ",carbon,"kg of CO2")
total+=carbon
print()

# flight calc 
dm = int(input("What is your total domestic flight hours : "))
inte = int(input("What is your total international flight hours :"))
print("Your flight carbon footprint is : ",flightCalc(inte,dm),"kg of CO2")
total+=flightCalc(inte,dm)
print()

# ice melted 
print("The total amount of Carbon Emission by you is : ",total,"kg of CO2")
print("That amount of Carbon is responsible for melting ",total*650,"kg of polar ice")
