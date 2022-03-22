import tkinter as tk
from tkinter import ttk

# for getting the city data
def getCities(filename):
    cities = []
    with open(filename, "r") as f:
        cities = f.read()
        cities = cities.split("\n")
        f.close()

    # Remove last element since it is an empty string
    cities.pop(len(cities)-1)

    # Append ", TX" to all cities
    newcit = []
    for city in cities:
        newcit.append(city+", TX")
    
    return newcit

def getStates(filename):
    states = []
    with open(filename, "r") as f:
        states = f.read()
        states = states.split("\n")
        f.close()

    # Remove last element since it is an empty string
    states.pop(len(states)-1)

    # Append "ian" to all states
    newstat = []
    for state in states:
        newstat.append(state+"ian")
    
    return newstat

def getKeyb(filename):
    key = []
    with open(filename, "r") as f:
        key = f.read()
        key = key.split("\n")
        f.close()

    # Remove last element since it is an empty string
    key.pop(len(key)-1)

    return key

def backBtn():
    currTab = tabControl.index("current")
    tabControl.tab(currTab-1, state="normal")
    tabControl.select(currTab-1)
    tabControl.tab(currTab, state="disabled")
#    __  ______   _____ ______________  ______ 
#   / / / /  _/  / ___// ____/_  __/ / / / __ \
#  / / / // /    \__ \/ __/   / / / / / / /_/ /
# / /_/ // /    ___/ / /___  / / / /_/ / ____/ 
# \____/___/   /____/_____/ /_/  \____/_/      
                                             

# Create window
root = tk.Tk()
root.title("bOSs Intaller")

# set window size
root.geometry("600x200")

# setting up tabs
tabControl = ttk.Notebook(root)
timezone = ttk.Frame(tabControl)
lang = ttk.Frame(tabControl)
keyboard = ttk.Frame(tabControl)
part = ttk.Frame(tabControl)
users = ttk.Frame(tabControl)
summary = ttk.Frame(tabControl)
install = ttk.Frame(tabControl)

tabControl.add(timezone, text="Timezone")
tabControl.add(lang, text="Language", state="disabled")
tabControl.add(keyboard, text="Keyboard Layout", state="disabled")
tabControl.add(part, text="Partitions", state="disabled")
tabControl.add(users, text="Users", state="disabled")
tabControl.add(summary, text="Summary", state="disabled")
tabControl.add(install, text="Installation", state="disabled")

tabControl.pack(expand=1, fill="both")

#    __  ______   __________  ____  ______
#   / / / /  _/  / ____/ __ \/ __ \/ ____/
#  / / / // /   / /   / / / / / / / __/   
# / /_/ // /   / /___/ /_/ / /_/ / /___   
# \____/___/   \____/\____/_____/_____/   

######################
# Timezone Selection #
######################

# Button time yay
def confirm():
    tabControl.tab(1, state="normal")
    tabControl.tab(0, state="disabled")
    tabControl.select(tab_id=1)

ttk.Label(timezone, text=" "*50).grid(column=0, row=2, sticky="W")
button = ttk.Button(timezone, text="Confirm", state="disabled", command=confirm)
button.grid(column=0, row=3, sticky="W")

# Working with the drop down to get the selected city
def getSel(event):
    ttk.Label(timezone, text=" "*60).grid(column=0, row=2, sticky="W")
    if drop.get() in ["El Paso, TX", "Socorro, TX"]:
        ttk.Label(timezone, text="Please select a valid continent").grid(column=0, row=2, sticky="W")
        button["state"] = tk.DISABLED
    else:
        button["state"] = tk.NORMAL

# get all options
options = getCities("texasCities.txt")

# set a title
ttk.Label(timezone, text="Timezone Selection", font=("Times", 24)).grid(column=0, row=0)

# create label, anchored to the right side of the cell it is in
lab = ttk.Label(timezone, text="Select Country for timing zone")
lab.grid(column=0, row=1, sticky="NW", pady=10)

# create a drop down menu, anchored to the Left side of the cell it is in
drop = ttk.Combobox(timezone, values=options, height=20, state="readonly")
drop.grid(column=1, row=1, sticky="NE", pady=10)
drop.bind("<<ComboboxSelected>>", getSel)

######################
# Language Selection #
######################

def confirml():
    tabControl.tab(2, state="normal")
    tabControl.select(tab_id=2)
    tabControl.tab(1, state="disabled")

ttk.Label(lang, text=" "*50).grid(column=0,row=2, sticky="W")
buttonl = tk.Button(lang, text="Confirm", state="disabled", command=confirml)
buttonl.grid(column=0, row=3, sticky="W")
def getSell(event):
    ttk.Label(lang, text=" "*60).grid(column=0, row=2, stick="W")
    buttonl["state"] = tk.NORMAL

optionsl = getStates("states.txt")
ttk.Label(lang, text="Language Selection", font=("Times", 24)).grid(column=0, row=0)

labl = ttk.Label(lang, text="Select Language")
labl.grid(column=0, row=1, sticky="NW", pady=10)

dropl = ttk.Combobox(lang, values=optionsl, height=20, state="readonly")
dropl.grid(column=1, row=1, sticky="NE", pady=10)
dropl.bind("<<ComboboxSelected>>", getSell)

# Back button
ttk.Button(lang, text="Back", command=backBtn).grid(column=1, row=3, sticky="NE")

######################
# Keyboard Selection #
######################

def confirmk():
    tabControl.tab(3, state="normal")
    tabControl.select(tab_id=3)
    tabControl.tab(2, state="disabled")

ttk.Label(keyboard, text=" "*50).grid(column=0,row=2, sticky="W")
buttonk = tk.Button(keyboard, text="Confirm", state="disabled", command=confirmk)
buttonk.grid(column=0, row=3, sticky="W")
def getSelk(event):
    ttk.Label(keyboard, text=" "*60).grid(column=0, row=2, stick="W")
    buttonk["state"] = tk.NORMAL

optionsk = getKeyb("state.txt")
ttk.Label(keyboard, text="Keyboard Selection", font=("Times", 24)).grid(column=0, row=0)

labk = ttk.Label(keyboard, text="Select Keyboard Layout")
labk.grid(column=0, row=1, sticky="NW", pady=10)

dropk = ttk.Combobox(keyboard, values=optionsk, height=20, state="readonly")
dropk.grid(column=1, row=1, sticky="NE", pady=10)
dropk.bind("<<ComboboxSelected>>", getSelk)

# Back button
ttk.Button(keyboard, text="Back", command=backBtn).grid(column=1, row=3, sticky="NE")
#     _______   ______     __  ______
#    / ____/ | / / __ \   / / / /  _/
#   / __/ /  |/ / / / /  / / / // /  
#  / /___/ /|  / /_/ /  / /_/ // /   
# /_____/_/ |_/_____/   \____/___/   

root.mainloop()

# TODO
#     ___        __              __   ____           __        ____         
#    /   | _____/ /___  ______ _/ /  /  _/___  _____/ /_____ _/ / /__  _____
#   / /| |/ ___/ __/ / / / __ `/ /   / // __ \/ ___/ __/ __ `/ / / _ \/ ___/
#  / ___ / /__/ /_/ /_/ / /_/ / /  _/ // / / (__  ) /_/ /_/ / / /  __/ /    
# /_/  |_\___/\__/\__,_/\__,_/_/  /___/_/ /_/____/\__/\__,_/_/_/\___/_/     
