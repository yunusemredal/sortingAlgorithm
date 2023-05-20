import time

from tkinter import ttk
def mergeSort(data,drawdata,timeTick):
    mergeAlgo(data,0,len(data)-1,drawdata,timeTick)

def mergeAlgo(data, left, right,drowdata,timeTick):

    if left < right:
        mid = int((left+right)/2)
        mergeAlgo(data,left, mid,drowdata,timeTick)
        mergeAlgo(data,mid+1, right,drowdata,timeTick)
        merge(data,left, mid, right,drowdata,timeTick)


def merge(data, left, mid, right,drawdata,timeTick):
    drawdata(data,ColorArray(len(data),left,mid,right))
    time.sleep(timeTick)
    leftPart = data[left:mid+1]
    rightPart = data[mid+1:right+1]
    leftIdx = rightIdx = 0
    for dataIdx in range(left,right):
        if leftIdx <len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx+=1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx+=1
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx+=1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx+=1
    drawdata(data,["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)

def ColorArray (Lenght,left,mid,right):
    colorArray = []
    for i in range(Lenght):
        if i >= left and i <= right:
            if i >= left and i <= mid:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")
    return colorArray