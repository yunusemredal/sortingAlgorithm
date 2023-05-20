import time
from tkinter import *
from tkinter import ttk
def partition(data,head,tail,drowData,timeTick):
    border=head
    pivot=data[tail]
    
    drowData(data,ColorArray(len(data),head,tail,border,border))
    time.sleep(timeTick)
    for j in range(head,tail):
        if data[j]<pivot:
            drowData(data,ColorArray(len(data),head,tail,border,j,True))
            time.sleep(timeTick)
            data[border],data[j]=data[j],data[border]
            border+=1
        drowData(data,ColorArray(len(data),head,tail,border,j))
        time.sleep(timeTick)

    drowData(data,ColorArray(len(data),head,tail,border,True))
    time.sleep(timeTick)
    data[border],data[tail]=data[tail],data[border]
    return border

def quickSort(data,head,tail,drowData,timeTick):
    if head < tail:
        partitionIdx= partition(data,head,tail,drowData,timeTick)

        quickSort(data, head,partitionIdx-1,drowData,timeTick)
        quickSort(data, partitionIdx+1,tail,drowData,timeTick)

def ColorArray(dataLen,head,tail,border,currIdx,isSwapping=False):
    colorArray=[]
    for i in range(dataLen):

        if i>= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')
        if i ==tail:
            colorArray[i]== 'orange'
        elif i == border:
            colorArray[i]== 'red'
        elif i == currIdx:
            colorArray[i ]== 'yellow'

            if isSwapping:
                if i== border and i== currIdx:
                    colorArray[i]== 'green'
    return colorArray
