def electricCalc(electricity_used, noOfFamMembers):
    return(((electricity_used*0.95)/noOfFamMembers)/30)

def vehicleCalc(distTravelled, mileage, noOfFamMembers, fuelType):
    if fuelType.lower()=="p":
        return(((distTravelled/mileage)*2.392)/noOfFamMembers)
    else:
        return(((distTravelled/mileage)*2.640)/noOfFamMembers) 

def flightCalc(domHours, intHours):
    return((((domHours*90)/75)+((intHours*90)/416))/365)

def iceCalc(carbon):
    return(carbon*650)


################################################################################################################################################################################################

from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import *
# 'pip install Pillow' for PIL


root = Tk()
root.title("Name of our prototype")
root.config(bg='#a3ddff')
root.geometry("700x1000")

Label(root, background = '#a3ddff', text = 'What is your name?', font = ('calibre',10, 'bold')).pack()
nameEntry = Entry(root,textvariable = StringVar, font=('calibre',10,'normal'))
nameEntry.pack(padx=10, pady=10)

Label(root, background = '#a3ddff', text = 'How many members are there in your family?', font=('calibre',10, 'bold')).pack()
familyMembersEntry = Entry(root,textvariable = StringVar, font=('calibre',10,'normal')) 
familyMembersEntry.pack(padx=10, pady=10)


Label(root, background = '#a3ddff', text = 'What is the amount of electrical energy you spend on an average each month? (in KiloWatt hour)', font=('calibre',10, 'bold')).pack()
ElectricityEntry = Entry(root,textvariable = DoubleVar, font=('calibre',10,'normal'))
ElectricityEntry.pack(padx=10, pady=10)



Label(root, background = '#a3ddff', text = 'Average distance covered by your vehicle per day? (Kilometres)', font=('calibre',10, 'bold')).pack()
vehicleDistance = Entry(root,textvariable = DoubleVar, font=('calibre',10,'normal'))
vehicleDistance.pack(padx=10, pady=10)

Label(root, background = '#a3ddff', text = 'Your mileage of your vehicle?', font=('calibre',10, 'bold')).pack()
mileage = Entry(root,textvariable = DoubleVar, font=('calibre',10,'normal'))
mileage.pack(padx=10, pady=10)

Label(root, background = '#a3ddff', text = 'Enter \'p\' for petrol vehicle and \'d\' for deisel', font=('calibre',10, 'bold')).pack()
fuelType = Entry(root,textvariable = StringVar, font=('calibre',10,'normal'))
fuelType.pack(padx=10, pady=10)


Label(root, background = '#a3ddff', text = 'Enter total hours of Domestic flights last year' , font=('calibre',10, 'bold')).pack()
DHours = Entry(root, textvariable=DoubleVar,font=('calibre',10,'normal'))
DHours.pack(padx=10, pady=10)


Label(root, background = '#a3ddff', text = 'Enter total hours of International flights last year' , font=('calibre',10, 'bold')).pack()
IHours = Entry(root, textvariable=DoubleVar,font=('calibre',10,'normal'))
IHours.pack(padx=10, pady=10)

#####################################################################################################################
carbon = 0
def CalculateCarbonFootprint():
    electricity = float(ElectricityEntry.get())
    famMem = int(familyMembersEntry.get())
    domestic = float(DHours.get())
    international = float(IHours.get())
    dist = float(vehicleDistance.get())
    mil = float(mileage.get())
    fType = fuelType.get()
    carbon = electricCalc(electricity, famMem) + flightCalc(international, domestic) + vehicleCalc(dist, mil, famMem, fType)
    ans.configure(text = "Your carbon footprint is: " + str(carbon*365)+" kg per year and "+str(carbon*30)+" kg per month.", font=('calibre',10,'normal'))
    displayTurtles(carbon,nameEntry.get())

Button(root, text = "I entered all details ", command = CalculateCarbonFootprint ,padding="3px").pack()
ans = Label(root, background = '#a3ddff', text = "", font=('calibre',10,'normal'))
ans.pack()



images = [PhotoImage(file="happyT.png"), PhotoImage(file="sad1.png"), PhotoImage(file="sad2.png"), PhotoImage(file="sad3.png"),PhotoImage(file="sadice.png")]

# display based on yearly emissions
def displayTurtles(carbonVal,name) :
    carbonVal*=365
    if carbonVal < 2000 :
        
        Label(root, justify = CENTER, background = '#a3ddff', text = f"You are very responsible {name}, Joe is very happy  ", image = images[0], compound='top', font=('calibre',13,'bold'), wraplength=500).pack()
        Label(root, justify = CENTER, background = '#a3ddff',foreground="#333333",text = "Joe is a critically endangered leatherback turtle,climate change impacts the Leatherback in two main ways: an increase in the temperature of nesting sands causes a greater proportion of females to hatch, destabilizing future populations; and sea level rise and stronger, more frequent storms erode nesting beaches and wash away eggs and hatchlings.", wraplength=500,font=('calibre',10,'normal')).pack()
        
    elif carbonVal < 4000 :
        
        Label(root, justify = CENTER, background = '#a3ddff', image = images[1], text = f"Poor Joe is very scared. {name}, please control your carbon emissions." , font=('calibre',13,'bold'), compound = 'top', wraplength=500).pack()
        Label(root, justify = CENTER, background = '#a3ddff',foreground="#333333",text = "Joe is a critically endangered leatherback turtle, climate change impacts the Leatherback in two main ways: an increase in the temperature of nesting sands causes a greater proportion of females to hatch, destabilizing future populations, and sea level rise and stronger, more frequent storms erode nesting beaches and wash away eggs and hatchlings.", wraplength=600,font=('calibre',10,'normal')).pack()
        
    elif carbonVal < 6000 :

        Label(root, justify = CENTER, background = '#a3ddff', image = images[2], text = f"{name}Your carbon emissions are way beyond normal, You made Poor Joe boy sad." , font=('calibre',13,'bold'), wraplength=500, compound = 'top').pack()
        Label(root, justify = CENTER, background = '#a3ddff',foreground="#333333",text = "Joe is a critically endangered leatherback turtle,climate change impacts the Leatherback in two main ways: an increase in the temperature of nesting sands causes a greater proportion of females to hatch, destabilizing future populations; and sea level rise and stronger, more frequent storms erode nesting beaches and wash away eggs and hatchlings.", wraplength=600,font=('calibre',10,'normal')).pack()

    elif carbonVal < 8000 : 
        Label(root, justify = CENTER, background = '#a3ddff', image = images[3], text = f"{name}Your carbon footprint is larger then bigfoot's,Poor Joe is worried about if he will be able to see his species existing in the near future" , font=('calibre',13,'bold'), compound = 'top', wraplength=500).pack()
        Label(root, justify = CENTER, background = '#a3ddff',foreground ="#333333",text = "Joe is a critically endangered leatherback turtle,climate change impacts the Leatherback in two main ways: an increase in the temperature of nesting sands causes a greater proportion of females to hatch, destabilizing future populations; and sea level rise and stronger, more frequent storms erode nesting beaches and wash away eggs and hatchlings.", wraplength=600,font=('calibre',10,'normal')).pack()
    
    else:
        Label(root, justify = CENTER, background = '#a3ddff',image = images[4],text = f"You are responsible for {iceCalc(carbonVal)} kgs of ice melting in polar regions in a year, resulting in rising sea levels and climate change effects.",font=('calibre',13,'bold'), compound = 'top', wraplength=500).pack()
        Label(root, justify = CENTER, background = '#a3ddff',foreground="#333333",text = f"{name}, your carbon emissions are highly dangerous to the planet as a whole, polar bears are losing their habitat because of this." , wraplength=600, font=('calibre',13,'normal')).pack()      
        


root.mainloop()
