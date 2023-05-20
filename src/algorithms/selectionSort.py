import time
from tkinter import *
from tkinter import ttk

def selectionSort(data, drowData, timeTick):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        drowData(data, ['yellow' if x == i or x == min_idx else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    drowData(data, ['green' for x in range(len(data))])


