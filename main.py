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

root = Tk()
root.title("Name of our prototype")
root.geometry("700x800")
root.mainloop()
