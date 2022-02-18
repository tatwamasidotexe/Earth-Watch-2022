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

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Name of our prototype")
root.geometry("700x800")

Label(root, text = 'What is your name?', font=('calibre',10, 'bold')).pack()
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
pd = Entry(root,textvariable = StringVar, font=('calibre',10,'normal'))
pd.pack()


Label(root, text = 'Enter total hours of Domestic flights last year' , font=('calibre',10, 'bold')).pack()
DHours = Entry(root, textvariable=IntVar,font=('calibre',10,'normal'))
DHours.pack()


Label(root, text = 'Enter total hours of International flights last year' , font=('calibre',10, 'bold')).pack()
IHours = Entry(root, textvariable=IntVar,font=('calibre',10,'normal'))
IHours.pack()

#####################################################################################################################
carbon = 0
def CalculateCarbonFootprint():
    global carbon
    electricity = ElectricityEntry.get()
    electricity = int(electricity)
    famMem = familyMembersEntry.get()
    famMem = int(famMem)
    domestic = DHours.get()
    domestic = int(domestic)
    international = IHours.get()
    international = int(international)
    dist = vehicleDistance.get()
    dist = int(dist)
    mil = mileage.get()
    mil= int(mil)
    p_d = pd.get()
    carbon = electricCalc(electricity,famMem)+flightCalc(domestic,international)+vehicleCalc(dist,mil,famMem,p_d)
    ans.configure(text = "Your carbon footprint is: "+str(carbon))

Button(root, text="I entered all details ", command = CalculateCarbonFootprint).pack()
ans = Label(root,text = "The carbon emmission")
ans.pack()

root.mainloop()
