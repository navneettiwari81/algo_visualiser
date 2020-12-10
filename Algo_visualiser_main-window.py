from tkinter import *
from tkinter import ttk
from os import system
from threading import Thread
from time import sleep
rooot=Tk()
Algo_visualiser_sorting="python "+r"Algo_visualiser_sorting.py"
rooot.title("ALGO VISUALISER")
rooot.config(bg="black")
rooot.maxsize(340,200)

def open_sorting_visualiser():
    system("python Algo_visualiser_sorting.py")
    
def open_path_finding():
    system("python path_finding_algo_a_star.py")
    

frame_1=Frame(rooot,width=320,height=180,bg="grey")
frame_1.grid(row=0,column=0,padx=10,pady=10,sticky=W+E)
Button(frame_1,text="SORTING ALGO VISUALISER",command=lambda:Thread(target=open_sorting_visualiser).start(),font=("TOKYO",16),bg="green").grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)
Button(frame_1,text=" PATH FINDING VISUALISER ",command=lambda:Thread(target=open_path_finding).start(),font=("TOKYO",16),bg="green").grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky=W)
rooot.mainloop()