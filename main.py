def electricCalc(electricity_used, noOfFamMembers):
    return((electricity_used*0.95)/noOfFamMembers)

def vehicleCalc(distTravelled, mileage, noOfFamMembers, fuelType):
    if fuelType.lower()=="p":
        return(((distTravelled/mileage)*2.392)/noOfFamMembers)
    else:
        return(((distTravelled/mileage)*2.640)/noOfFamMembers)      

def flightCalc(domHours, intHours):
    total = 0
    total+=((domHours*90)/75)
    total+=((intHours*90)/416)
    return(total/365)

def iceCalc(carbon):
    return(carbon*650)

################################################################################################################################################################################################

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Name of our prototype")
root.geometry("700x800")

Label(root, text = 'What is your name?', font = ('calibre',10, 'bold')).pack()
nameEntry = Entry(root,textvariable = StringVar, font=('calibre',10,'normal'))
nameEntry.pack()

Label(root, text = 'How many members are there in your family?', font=('calibre',10, 'bold')).pack()
familyMembersEntry = Entry(root,textvariable = StringVar, font=('calibre',10,'normal')) 
familyMembersEntry.pack()


Label(root, text = 'What is the amount of electical energy spent on an average each day? (in KiloWatt hour)', font=('calibre',10, 'bold')).pack()
ElectricityEntry = Entry(root,textvariable = IntVar, font=('calibre',10,'normal'))
ElectricityEntry.pack()

Label(root, text = 'Number of vehicles you own?', font=('calibre',10, 'bold')).pack()
noOfVehicles = Entry(root,textvariable = IntVar, font=('calibre',10,'normal'))
noOfVehicles.pack()

# map to store details for each vehicle
vehicleDeets = {
    'distanceTravelled' : []
}

vNumber = getint(noOfVehicles.get()) # ValueError: invalid literal for int() with base 10: ''

# loop to get distance travelled by each of the n vehicles owned by the user
# checking the loop for only one vehicle detail for now
for i in range(1, vNumber+1) :
    Label(root, text = 'Average distance covered by vehicle ' + i + ' per day?(Kilometres)', font=('calibre',10, 'bold')).pack()
    vehicleDistance = Entry(root,textvariable = IntVar, font=('calibre',10,'normal'))
    vehicleDistance.pack()
    vehicleDeets['distanceTravelled'].append(int(vehicleDistance))

Label(root, text = 'Your mileage', font=('calibre',10, 'bold')).pack()
mileage = Entry(root,textvariable = IntVar, font=('calibre',10,'normal'))
mileage.pack()

Label(root, text = 'Enter \'p\' for petrol vehicle and \'d\' for deisel', font=('calibre',10, 'bold')).pack()
fuelType = Entry(root,textvariable = StringVar, font=('calibre',10,'normal'))
fuelType.pack()


Label(root, text = 'Enter total hours of Domestic flights last year' , font=('calibre',10, 'bold')).pack()
DHours = Entry(root, textvariable=IntVar,font=('calibre',10,'normal'))
DHours.pack()


Label(root, text = 'Enter total hours of International flights last year' , font=('calibre',10, 'bold')).pack()
IHours = Entry(root, textvariable=IntVar,font=('calibre',10,'normal'))
IHours.pack()

#####################################################################################################################
carbon = 0
def CalculateCarbonFootprint():
    electricity = int(ElectricityEntry.get())
    famMem = int(familyMembersEntry.get())
    domestic = int(DHours.get())
    international = int(IHours.get())
<<<<<<< HEAD
    # international = int(international)
    # dist = int(vehicleDistance.get())
    # dist = int(dist)
=======
    dist = int(vehicleDistance.get())
>>>>>>> 1c6a34c0c70089c5a71b30525d3f28bcee35e7bb
    mil = int(mileage.get())
    fType = fuelType.get()
    carbon = electricCalc(electricity, famMem) + flightCalc(international, domestic) + vehicleCalc(0, mil, famMem, fType)
    ans.configure(text = "Your carbon footprint is: " + str(carbon))

Button(root, text = "I entered all details ", command = CalculateCarbonFootprint).pack()
ans = Label(root, text = "The carbon emmission")
ans.pack()

root.mainloop()
