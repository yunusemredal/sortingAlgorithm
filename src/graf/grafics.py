import matplotlib.pyplot as plt
import numpy as np

def drawRootGraph():
    # Kök grafik için verileri oluşturun
    x = np.linspace(0, 10, 100)
    y = np.sqrt(x)

    # Kök grafik oluşturun
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)

    # Grafik özelliklerini ayarlayın
    plt.xlabel('X Değeri')
    plt.ylabel('Kök(X) Değeri')
    plt.title('Kök Grafik')

    # Grafikleri gösterin
    plt.show()

import tkinter as tk
import math

def drawRootGraph():
    root = tk.Tk()
    root.title("Kök Grafik")

    canvas_width = 800
    canvas_height = 600

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    x_start = 0
    x_end = 10
    num_points = 100
    dx = (x_end - x_start) / num_points

    for i in range(num_points):
        x = x_start + i * dx
        y = math.sqrt(x)

        x_pixel = canvas_width * (x - x_start) / (x_end - x_start)
        y_pixel = canvas_height - canvas_height * (y / math.sqrt(x_end))

        canvas.create_oval(x_pixel, y_pixel, x_pixel + 2, y_pixel + 2, fill="black")

    root.mainloop()

# Kök grafik fonksiyonunu çağırın
drawRootGraph()