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
    return(total)

def iceCalc(carbon):
    return(carbon*650)

from tkinter import *
from tkinter import ttk 

root = Tk()
root.title("Name of our prototype")
root.geometry("700x800")

nameLabel = Label(root, text = 'What is your name?', font=('calibre',10, 'bold'))
name_entry = Entry(root,textvariable = StringVar, font=('calibre',10,'normal'))

familyMembersLabel = Label(root, text = 'How many members are there in your family?', font=('calibre',10, 'bold'))
familyMembersEntry = Entry(root,textvariable = StringVar, font=('calibre',10,'normal')) 


ElectricityLabel = Label(root, text = 'What is the amount of electical energy spent on an average each day? (in KiloWatt hour)', font=('calibre',10, 'bold'))
ElectricityEntry = Entry(root,textvariable = IntVar, font=('calibre',10,'normal'))


VehicleLabel = Label(root, text = 'Number of vehicles you own?', font=('calibre',10, 'bold'))
VehicleEntry = Entry(root,textvariable = IntVar, font=('calibre',10,'normal'))

variables = []

def calc(a,b,c,f):
    return (a/b)*2.3 /f

carbon = 0
for i in range(int(VehicleEntry.get())):
    var = IntVar()
    dLable = Label(root, text = 'How much distance is covered on an average per day on this vehicle?', font=('calibre',10, 'bold'))
    d = Entry(root, textvariable=var, font=('calibre',10,'normal'))
    root.grid(row=i+1, column=0)
    variables.append(var)



root.mainloop()
