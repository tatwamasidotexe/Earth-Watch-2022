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
from PIL import ImageTk,Image  
# 'pip install Pillow' for PIL


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



Label(root, text = 'Averge distance covered by your vehicle per day?(Kilometres)', font=('calibre',10, 'bold')).pack()
vehicleDistance = Entry(root,textvariable = IntVar, font=('calibre',10,'normal'))
vehicleDistance.pack()

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
    dist = int(vehicleDistance.get())
    mil = int(mileage.get())
    fType = fuelType.get()
    carbon = electricCalc(electricity, famMem) + flightCalc(international, domestic) + vehicleCalc(dist, mil, famMem, fType)
    ans.configure(text = "Your carbon footprint is: " + str(carbon))
    displayTurtles(carbon)

Button(root, text = "I entered all details ", command = CalculateCarbonFootprint).pack()
ans = Label(root, text = "The carbon emmission")
ans.pack()

canvas = Canvas(root, width=300, height=400)
canvas.pack(side='bottom')
img = ImageTk.PhotoImage(Image.open("happyT.jpeg"))

def displayTurtles(carbonVal) :
    if carbonVal < 10 :
        canvas.create_image(10,10, anchor=NW, image=img)

root.mainloop()