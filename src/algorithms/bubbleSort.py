import time
from tkinter import *
from tkinter import ttk

def bubbleSort(data, drowData,timeTick):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drowData(data,['yellow' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
    drowData(data,['green' for x in range(len(data))])



def bubble_sort(data,drowdata):
    size = len(data)
    for i in range(size):
        swapped = False
        for j in range(size - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                drowdata(data)
                time.sleep(0.2)
        if not swapped:
            break
    #return data
    return data
