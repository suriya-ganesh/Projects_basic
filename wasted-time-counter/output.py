from tkinter import *
from tkinter import ttk
from tkinter import font
from calcs import *
import time
import datetime
from datetime import timedelta

print (days)

def quit(*args):
	root.destroy()
	
def clock_time():
	time = datetime.datetime.now()
	time = (time.strftime("%H:%M:%S"))
	
	
	txt.set(time)
	years_text.set("%r YEARS...."%age)
	days_text.set("%r DAYS....."%age_days)
	shit_speak.set("TIME SPENT, WASTING OXYGEN")
	
	
	root.after(1000, clock_time)
	

root = Tk()
root.attributes("-fullscreen", False)
root.configure(background = 'red')
root.bind("X", quit)
root.after(1000,clock_time)
#set(age, age_days, days)

fnt = font.Font(family = 'Helvetica', size = 40, weight = 'bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = "white", background = "black")
lbl.place(relx = 0.5, rely = 0.8, anchor = CENTER)

fnt = font.Font(family = 'Helvetica', size = 15, weight = 'bold')
years_text = StringVar()
lbl = ttk.Label(root, textvariable = years_text, font = fnt, foreground = "white", background = "black")
lbl.place(relx = 0.5, rely = 0.3, anchor = CENTER)

fnt = font.Font(family = 'Helvetica', size = 15, weight = 'bold')
days_text = StringVar()
lbl = ttk.Label(root, textvariable = days_text, font = fnt, foreground = "white", background = "black")
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

fnt = font.Font(family = 'Helvetica', size = 12, weight = 'bold')
shit_speak = StringVar()
lbl = ttk.Label(root, textvariable = shit_speak, font = fnt, foreground = "white", background = "black")
lbl.place(relx = 0.5, rely = 0.09, anchor = CENTER)

root.mainloop()