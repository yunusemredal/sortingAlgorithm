import time
from tkinter import *
from tkinter import ttk

def insertionSort(data, drowData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            drowData(data, ['yellow' if x == j + 1 else 'red' for x in range(len(data))])
            time.sleep(timeTick)
        data[j + 1] = key
    drowData(data, ['green' for x in range(len(data))])


