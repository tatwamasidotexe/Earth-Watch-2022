def electricCalc(amused,nf):
    
    return((amused*0.95)/nf)

def vehicleCalc(distance,mil,nf,type):
    print(nf,mil)
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

################################################################################################################################################################################################

from tkinter import *
from tkinter import ttk 

root = Tk()
root.title("Name of our prototype")
root.geometry("700x800")

nameLabel = Label(root, text = 'What is your name?', font=('calibre',10, 'bold'))
nameLabel.pack()
nameEntry = Entry(root,textvariable = StringVar, font=('calibre',10,'normal'))
nameEntry.pack()

familyMembersLabel = Label(root, text = 'How many members are there in your family?', font=('calibre',10, 'bold'))
familyMembersLabel.pack()
familyMembersEntry = Entry(root,textvariable = StringVar, font=('calibre',10,'normal')) 
familyMembersEntry.pack()


ElectricityLabel = Label(root, text = 'What is the amount of electical energy spent on an average each day? (in KiloWatt hour)', font=('calibre',10, 'bold'))
ElectricityLabel.pack()
ElectricityEntry = Entry(root,textvariable = IntVar, font=('calibre',10,'normal'))
ElectricityEntry.pack()


VehicleLabel = Label(root, text = 'Number of vehicles you own?', font=('calibre',10, 'bold'))
VehicleLabel.pack()
VehicleEntry = Entry(root,textvariable = IntVar, font=('calibre',10,'normal'))
VehicleEntry.pack()

#carbon = 0


def vehicle():
    a = VehicleEntry.get()
    a = int(a)
    print (a)
    carbon = []
    
    for i in range(a):

        
        Label(root, text = 'How much distance is covered on an average per day on this vehicle?', font=('calibre',10, 'bold')).pack()
        d = Entry(root, textvariable=IntVar, font=('calibre',10,'normal')).pack()
        
        Label(root, text = 'What is the mileage of this vehicle?', font=('calibre',10, 'bold')).pack()
        m = Entry(root, textvariable=IntVar, font=('calibre',10,'normal')).pack()
        
        Label(root, text = 'Petrol or deisel(p/d)', font=('calibre',10, 'bold')).pack()
        p = Entry(root, textvariable=IntVar, font=('calibre',10,'normal')).pack()
    
        def TakeInput():
            carbon.append(vehicleCalc(int(d.get()),int(m.get()),int(familyMembersEntry.get()),p.get()))
        
        Button(root, text = "Enter for next vehicle",command = TakeInput).pack()
        
        root.grid(row=i+1, column=0)
             
        
        

ibutton = Button(root, text="Enter details for vehicles", command = vehicle).pack()
variables = []

def calc(a,b,c,f):
    return (a/b)*2.3 /f





root.mainloop()
