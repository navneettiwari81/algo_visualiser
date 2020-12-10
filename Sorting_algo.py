import time

#COLOR CODES:
#"#4682B4":bluish
#"#1ec9b5":parrot Greenish
#"#008080":Backish Blue

#Bubble Sort
#
#
#space to seperate different sorting algo's
#
#

def bubble_sort(data_array,draw_on_canvas,speed):
    def_speed=1.0
    for _ in range(len(data_array)-1):
        for j in range(len(data_array)-1):
            if data_array[j]>=data_array[j+1]:
                data_array[j],data_array[j+1]=data_array[j+1],data_array[j]
                draw_on_canvas(data_array,["green" if i==j or i==j+1 else "#4682B4" for i in range(len(data_array))])
                time.sleep(def_speed/(speed))
    draw_on_canvas(data_array,["green" for i in range(len(data_array))])

#Insertion Sort
#
#
#space to seperate different sorting algo's
#
#
    
def insertion_sort(data_array,draw_on_canvas,speed):
    def_speed=1.0
    for i in range(1,len(data_array)):
        key=data_array[i]
        j=i-1
        draw_on_canvas(data_array,["red" if x==i  else "#4682B4" for x in range(len(data_array))])
        time.sleep(def_speed/(speed))
        while(j>=0 and data_array[j]>key):
            data_array[j+1],data_array[j]=data_array[j],data_array[j+1]
            draw_on_canvas(data_array,["green" if x==j or x==j+1 else "#4682B4" for x in range(len(data_array))])
            time.sleep(def_speed/(speed))
            j=j-1
        data_array[j+1]=key
        #draw_on_canvas(data_array,["green" if x==i or x==j+1 else "#4682B4" for x in range(len(data_array))])
        
    draw_on_canvas(data_array,["green" for i in range(len(data_array))])
  
#Selection Sort
#
#
#space to seperate different sorting algo's
#
#
    
def selection_sort(data_array,draw_on_canvas,speed):
    def_speed=1.0
    for i in range(len(data_array)-1):
        min=i
        draw_on_canvas(data_array,["red" if x==min else "#4682B4" for x in range(len(data_array))])
        time.sleep(def_speed/speed)
        for j in range(i+1,len(data_array)):
            if (data_array[j]<data_array[min]):
                min=j
            color=[]
            for _ in range(len(data_array)):
                if _==min:
                    color.append("red")
                elif _ ==j:
                    color.append("green")
                elif _==i:
                    color.append("gray")
                else:
                    color.append("#4682B4")
            draw_on_canvas(data_array,color)
            time.sleep(def_speed/speed)
        data_array[i],data_array[min]=data_array[min],data_array[i]
        draw_on_canvas(data_array,["green" if x==min or x==i else "#4682B4" for x in range(len(data_array))])
        time.sleep(def_speed/speed)
    draw_on_canvas(data_array,["green" for i in range(len(data_array))])
    
#Shell Sort
#
#
#space to seperate different sorting algo's
#
#
    
def shell_sort(data_array,draw_on_canvas,speed):
    n=len(data_array)
    gap=n//2
    def_speed=1.0
    while(gap>0):
        #draw_on_canvas(data_array,[])
        for i in range(gap,n):
            draw_on_canvas(data_array,["green" if  x==i-gap or x==i else "#4682B4" for x in range(n)])
            time.sleep(def_speed/speed)
            temp=data_array[i]
            j=i
            while(j>=gap and data_array[j-gap]>temp):
                color=[]
                for _ in range(n):
                    if _==j-gap:
                        color.append("red")
                    elif _ ==j:
                        color.append("green")
                    else:
                        color.append("#4682B4")
                draw_on_canvas(data_array,color)
                time.sleep(def_speed/speed)
                data_array[j]=data_array[j-gap]
                j-=gap
            draw_on_canvas(data_array,["green" if x==j or x==i else "#4682B4" for x in range(n)])
            time.sleep(def_speed/speed)
            data_array[j]=temp
        gap=gap//2
        draw_on_canvas(data_array,["green" for _ in range(n)])
 

#QUICK sort
#
#
#space to seperate different sorting algo's
#
#
def partition(data_array,head,tail,draw_on_canvas,speed):
    border=head
    def_speed=1.0
    pivot=data_array[tail]
    
    draw_on_canvas(data_array,color_array_fncn_quick_sort(len(data_array),head,tail,border,border))
    time.sleep(def_speed/speed)
    for j in range(head,tail):
        if data_array[j]<pivot:
            draw_on_canvas(data_array,color_array_fncn_quick_sort(len(data_array),head,tail,border,j,True))
            time.sleep(def_speed/speed)
            data_array[border],data_array[j]=data_array[j],data_array[border]
            border +=1
    
        draw_on_canvas(data_array,color_array_fncn_quick_sort(len(data_array),head,tail,border,j))
        time.sleep(def_speed/speed)
    data_array[border],data_array[tail]=data_array[tail],data_array[border]
    
    return border

def quick_sort(data_array,head,tail,draw_on_canvas,speed):
    if head<tail:
        partition_index=partition(data_array,head,tail,draw_on_canvas,speed)
    
        quick_sort(data_array,head,partition_index-1,draw_on_canvas,speed)
        quick_sort(data_array,partition_index+1,tail,draw_on_canvas,speed)
    
def color_array_fncn_quick_sort(n,head,tail,border,current_index,swapping=False):
    color_array=[]
    for i in range(n):
        if i>=head and i<=tail:
            color_array.append("gray")
        else:
            color_array.append("#4682B4")
        
        if i==tail:
            color_array[i]="white"
        elif i==border:
            color_array[i]="red"
        elif i==current_index:
            color_array[i]="#008080"
        
        if swapping:
            if i==border or i==current_index:
                color_array[i]="green"
    
    return color_array

#Merge Sort
#
#
#space to seperate different sorting algo's
#
#
def merge_sort(data_array,draw_on_canvas,speed):
    def_speed=1.0
    merge_sort_main(data_array,0,len(data_array)-1,draw_on_canvas,def_speed/speed)
    draw_on_canvas(data_array,["green" for x in range(len(data_array))])
    
def merge_sort_main(data_array,left,right,draw_on_canvas,speed):
    if left<right:
        middle=(left+right)//2
        merge_sort_main(data_array,left,middle,draw_on_canvas,speed)
        merge_sort_main(data_array,middle+1,right,draw_on_canvas,speed)
        merge_array(data_array,left,middle,right,draw_on_canvas,speed)
        
def merge_array(data_array,left,middle,right,draw_on_canvas,speed):
    draw_on_canvas(data_array,color_array_merge(len(data_array),left,middle,right))
    time.sleep(speed)
    left_part=data_array[left:middle+1]
    right_part=data_array[middle+1:right+1]
    
    left_index=0
    right_index=0
    
    for index in range(left,right+1):
        if left_index<len(left_part) and right_index<len(right_part):
            if left_part[left_index]<=right_part[right_index]:
                data_array[index]=left_part[left_index]
                left_index+=1
            else:
                data_array[index]=right_part[right_index]
                right_index+=1
        elif left_index<len(left_part):
            data_array[index]=left_part[left_index]
            left_index+=1
        else:
            data_array[index]=right_part[right_index]
            right_index+=1
    
    draw_on_canvas(data_array,["green" if x >=left and x<=right else "white" for x in range(len(data_array))])
    time.sleep(speed)
    
def color_array_merge(n,left,middle,right):
    color_array=[]
    for i in range(n):
        if  i>=left and i<=right:
            if i<=middle:
                color_array.append("#EEE8AA")
            else:
                color_array.append("red")
        else:
            color_array.append("white")
    return color_array
    
    
    
    
    
    
    
    
    
    
    
    
    
