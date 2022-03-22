import tkinter as tk
from tkinter import ttk

# for getting language data
def getLangs(filename):
    langs = []
    with open(filename, "r") as f:
        langs = f.read()
        langs = langs.split("\n")
        f.close()
    # remove last element since empty string
    langs.pop(len(langs)-1)
    return langs


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

def confirmt():
    tabControl.tab(1, state="normal")
    tabControl.select(tab_id=1)

entryt = ttk.Entry(timezone, width=40)
entryt.focus_set()
entryt.pack()
buttont = tk.Button(timezone, text="Confirm", state="disabled", command=confirmt)

labt = ttk.Label(timezone, text="Enter Timezone (UTC)")
######################
# Language Selection #
######################

def confirml():
    tabControl.tab(2, state="normal")
    tabControl.select(tab_id=2)

ttk.Label(lang, text=" "*50).grid(column=0,row=2, sticky="W")
buttonl = tk.Button(lang, text="Confirm", state="disabled", command=confirml)
buttonl.grid(column=0, row=3, sticky="W")
def getSell(event):
    ttk.Label(lang, text=" "*60).grid(column=0, row=2, stick="W")
    buttonl["state"] = tk.NORMAL

optionsl = getLangs("langs.txt")
ttk.Label(lang, text="Language Selection", font=("Times", 24)).grid(column=0, row=0)

labl = ttk.Label(lang, text="Select Language")
labl.grid(column=0, row=1, sticky="NW", pady=10)

dropl = ttk.Combobox(lang, values=optionsl, height=20, state="readonly")
dropl.grid(column=1, row=1, sticky="NE", pady=10)
dropl.bind("<<ComboboxSelected>>", getSell)

#    _______   ______     __  ______
#   / ____/ | / / __ \   / / / /  _/
#  / __/ /  |/ / / / /  / / / // /  
# / /___/ /|  / /_/ /  / /_/ // /   
#/_____/_/ |_/_____/   \____/___/   

root.mainloop()
