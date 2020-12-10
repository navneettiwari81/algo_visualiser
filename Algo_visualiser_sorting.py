from tkinter import *
import random
from tkinter import ttk
from tkinter import messagebox
import Sorting_algo
from time_compare_sorting_algo import command
from threading import Thread

root=Tk()
root.title("SORTING ALGO VISUALISER")
root.maxsize(900,670)
root.config(bg="black")
operation_frame=Frame(root,width=880,height=100,bg="grey")
operation_frame.grid(row=0,column=0,padx=10,pady=5,sticky=W+E)

canvas=Canvas(root,width=880,height=480)
canvas.grid(row=1,column=0,padx=10,pady=5)

def generate():
    #Label(operation_frame,text=complexity[algo_variable.get()],font=("Helvetica",16),bg="grey").grid(row=0,column=5,padx=5,pady=5,sticky=W)
    custom_input=custom_input_entry.get()
    global data_array
    flag=True
    warning_flag=True
    if "," in custom_input:
        try:
            data_array=list(map(int,custom_input.split(",")))
            flag=False
            if len(data_array)<5:
                flag=True
        except:
            if custom_input!="Enter the elements seperated by space or comma." and warning_flag :
                messagebox.showwarning("Wrong Input","Wrong Input\nRandom Array will be Generated")
                warning_flag=False
            rndm()
    elif " " in custom_input:
        try:
            data_array=list(map(int,custom_input.split(" ")))
            flag=False
            if len(data_array)<5:
                flag=True
        except:
            if custom_input!="Enter the elements seperated by space or comma."  and warning_flag :
                messagebox.showwarning("Wrong Input","Wrong Input\n\nRandom Array will be Generated")
                warning_flag=False
            rndm()
    if flag:
        if custom_input!="Enter the elements seperated by space or comma."  and warning_flag :
            messagebox.showwarning("Warning","Input Size less than 5\nSystem will Generate a 10 size Array.")
            warning_flag=False
        rndm()

    draw_on_canvas(data_array,["#4682B4" for i in range(len(data_array))])
def rndm():
    global data_array
    try:
        size=int(arr_size.get())
    except:
        size=10
    try:
        min_value=int(min_entry.get())
    except:
        min_value=0
    try:
        max_value=int(max_entry.get())
    except:
        max_value=150
    algo=algo_variable.get()
    if size<5:
        size=5
    if size>50:
        size=50
    if min_value<0:
        min_value=0
    if max_value>150:
        max_value=150
    if min_value>max_value:
        max_value,min_value=min_value,max_value
    
    data_array=[]
    for i in range(size):
        data_array.append(random.randrange(min_value,max_value+1))
    


    
def draw_on_canvas(data_array,color_array): 
    canvas.delete("all")
    canvas_height=480
    canvas_width=880
    margin=15 #margin from left and right
    spacing=10 #space between each bar
    #calculate width of each bar
    bar_width=(canvas_width-(margin*2))/(len(data_array))
    
    #normalise the data 
    data_normalised=[i/max(data_array) for i in data_array]
    for i,height in enumerate(data_normalised):
        x_0= i*bar_width +spacing +margin
        y_0=canvas_height-height *440
        x_1=x_0+bar_width-spacing
        y_1=canvas_height
        canvas.create_rectangle(x_0,y_0,x_1,y_1,fill=color_array[i])
        canvas.create_text(x_0+3,y_0,anchor=SW,text=str(data_array[i]))
    root.update_idletasks()
def start():
    global data_array
    speed=int(speed_scale.get())
    if algo_variable.get()=="Bubble Sort":
        Sorting_algo.bubble_sort(data_array,draw_on_canvas,speed)
    elif algo_variable.get()=="Insertion Sort":
        Sorting_algo.insertion_sort(data_array,draw_on_canvas,speed)
    elif algo_variable.get()=="Selection Sort":
        Sorting_algo.selection_sort(data_array,draw_on_canvas,speed)
    elif algo_variable.get()=="Quick Sort":
        Sorting_algo.quick_sort(data_array,0,len(data_array)-1,draw_on_canvas,speed)
        draw_on_canvas(data_array,["green" for i in range(len(data_array))])
    elif algo_variable.get()=="Shell Sort":
        Sorting_algo.shell_sort(data_array,draw_on_canvas,speed)      
    elif algo_variable.get()=="Merge Sort":
        Sorting_algo.merge_sort(data_array,draw_on_canvas,speed)

#
#time analysis function
#
def time_analysis():
    temp=command()
    size_lst=temp[1]
    time_dict=temp[0]
    top=Toplevel()
    label_text="size\tBubble Sort\tInsertion Sort\tSelection Sort\n"
    label_text+="*"*80+"\n"
    for i,size in enumerate(size_lst[:5]):
        label_text+=str(size)+"\t  "+str("%0.5f"%(time_dict["Bubble Sort"][i]))+"\t\t"+str("%0.5f"%(time_dict["Insertion Sort"][i]))+"\t\t"+str("%0.5f"%(time_dict["Selection Sort"][i]))+"\n"
    Label(top,text=label_text,font=("Helvetica", 16),bg="green",).grid(row=0,column=0,padx=10,pady=10,sticky=W)
    


#
#
#
      
Label(operation_frame,text="Sorting Algorithm: ",activeforeground="red", font=("Helvetica", 16),bg="grey",anchor=W).grid(row=0,column=0,padx=5,pady=5,sticky=W)
#drop down menu for selecting algos
algo_variable=StringVar()
algo_variable.set("Bubble Sort")
algo_lst=["Bubble Sort",
          "Merge Sort",
          "Insertion Sort",
          "Selection Sort",
          "Quick Sort",
          "Shell Sort"
         ]
complexity={
    "Bubble Sort":"O(N)^2",
    "Merge Sort":"O(N)log(N)",
    "Insertion Sort":"O(N)^2",
    "Selection Sort":"O(N)^2"
}

drop_down=OptionMenu(operation_frame,algo_variable,*algo_lst)
drop_down.grid(row=0,column=1,padx=5,pady=5,sticky=W)

#enter and store the size of the array
Label(operation_frame,text="Size: ",bg="grey", font=("Helvetica", 16)).grid(row=1,column=0,padx=5,pady=5,sticky=W)
arr_size=Entry(operation_frame)
arr_size.grid(row=1,column=1,padx=5,pady=5,sticky=W)

#genarate button to generate the bars and array
Button(operation_frame,text="GENERATE", font=("Helvetica", 16),command=generate,bg="green").grid(row=0,column=2,padx=5,pady=5,sticky=W)

#max and min values for the array
Label(operation_frame,text="Max Value: ", font=("Helvetica", 16),bg="grey").grid(row=1,column=2,padx=5,pady=5,sticky=W)
Label(operation_frame,text="Min Value: ", font=("Helvetica", 16),bg="grey").grid(row=1,column=4,padx=5,pady=5,sticky=W)
max_entry=Entry(operation_frame,foreground="red")
max_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
min_entry=Entry(operation_frame,foreground="red")
min_entry.grid(row=1,column=5,padx=5,pady=5,sticky=W)

#Label(operation_frame,text="Time Complexity: ",font=("Helvetica",16),bg="grey").grid(row=0,column=3,columnspan=2,padx=5,pady=5,sticky=W)

speed_scale=Scale(operation_frame,from_=1,to=20.0,length=220,digits=2,resolution=0.1,orient=HORIZONTAL,label="Speed:")
speed_scale.grid(row=0,column=3,columnspan=2,padx=5,pady=5,sticky=W)
Button(operation_frame,text="START",font=("TOKYO", 16),command=start,bg="green").grid(row=0,column=5,padx=5,pady=5)
#analysis:
Label(operation_frame,text="Custom Input :", font=("Helvetica", 16),bg="grey").grid(row=2,column=0,padx=5,pady=5,sticky=W)
custom_input_var=StringVar()
custom_input_var.set("""Enter the elements seperated by space or comma.""")
custom_input_entry=Entry(operation_frame,width=40,background="white",foreground="red",font=("TOKYO",12),textvariable=custom_input_var)
custom_input_entry.grid(row=2,column=1,padx=5,pady=5,columnspan=3,sticky=W)
custom_input_entry.bind("<Double-1>",lambda event:custom_input_entry.delete(0,END))
Button(operation_frame,text="Time Analysis",font=("Helvetica", 16),command=Thread(target=time_analysis).start(),bg="#1ec9b5").grid(row=2,column=5,padx=5,pady=5,sticky=W)
root.mainloop()