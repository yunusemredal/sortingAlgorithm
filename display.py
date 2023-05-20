from tkinter import *
from tkinter import ttk
import random
from src.algorithms.bubbleSort import bubbleSort
from src.algorithms.quickSort import quickSort
from src.algorithms.mergeSort import mergeSort
from src.algorithms.insertionSort import insertionSort
from src.algorithms.selectionSort import selectionSort
from src.graf.grafics import drawRootGraph
root = Tk()
root.title('SIRALAMA ALGORİTMALARI GÖRSELLEŞTİRİCİSİ')
root.geometry('1100x800+200+80')
root.config(bg='White')
data = []

def drowData(data,colorArray):
    canvas.delete('all') #clear the canvas
    canvas_height=690
    canvas_width=850

    x_width= canvas_width/(len(data)+1)
    offset=10
    spacing_bet_rect=10
    normalized_data=[i/max(data) for i in data]

    for i , height in enumerate(normalized_data):
        x0=i*x_width+offset+spacing_bet_rect
        y0=canvas_height-height*400 #normalize data to fit the canvas 
                                    #one formula so taht our data won't exceed our canvas our convas
        x1=(i+1)*x_width
        y1=canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=('times new roman', 15, 'italic'), fill='orange')

    root.update_idletasks()


def startAlgorithm():
    global data
    if not data:
        return
    if algo_menu.get() == 'Bubble Sort':
        bubbleSort(data, drowData,speedScale.get())
    elif algo_menu.get() == 'Quick Sort':
        quickSort(data,0,len(data)-1,drowData,speedScale.get())
    elif algo_menu.get() == 'Merge Sort':
        mergeSort(data,drowData,speedScale.get())
    elif algo_menu.get() == 'Insertion Sort':
        insertionSort(data, drowData,speedScale.get())
    elif algo_menu.get() == 'Selection Sort':
        selectionSort(data, drowData,speedScale.get())
    drowData(data,['green' for x in range(len(data))])
    drawRootGraph()

def Generate():
    global data
    print("Selected Algorithm: " + selected_algorithm.get())
    miniValue = int(minValue.get())
    maxiValue = int(maxValue.get())
    sizeeValue = int(sizeValue.get())
    
    data = []
    for _ in range(int(sizeValue.get())):
        data.append(random.randrange(int(minValue.get()), int(maxValue.get()) + 1))
    drowData(data,['red'for x in range(len(data))])

#label button,speed scale
selected_algorithm = StringVar()

mainlabel = Label(root,text='Algoritma:',
                    font=('times new roman',16,'italic'),
                    width= 10, fg='black',bg='white',relief=GROOVE,bd=5)
mainlabel.place(x=0,y=0)
#combo box
algo_menu = ttk.Combobox(root, width=15,
                    font=('times new roman',19,'italic'),
                    textvariable= selected_algorithm,
                    values=['Bubble Sort','Insertion Sort',
                            'Merge Sort','Quick Sort','Selection Sort'])
algo_menu.place(x=125,y=0)
algo_menu.current(0)
#Buttonlar
random_generate= Button(root,text="Oluştur",bg='white',fg='black',
                        font=('times new roman',12,'italic'),
                        relief=SUNKEN,activebackground='white',
                        activeforeground='black',bd=5, width=10 ,
                        command=Generate)
random_generate.place(x=750,y=60)
start=Button(root,text="Start",bg='white',fg='black',
                        font=('times new roman',12,'italic'),
                        relief=SUNKEN,activebackground='white',
                        activeforeground='black',bd=5, width=10 ,
                        command=startAlgorithm)
start.place(x=750,y=0)
#Labellar
sizeValueLabel= Label(root,text='Boyut:',
                font=('times new roman',12,'italic'),
                width= 10,height=2, fg='black',bg='red',relief=GROOVE,bd=5)
sizeValueLabel.place(x=0,y=60)
sizeValue= Scale(root,from_=0,to=100 ,orient=HORIZONTAL,
                    font=('times new roman',14,'italic'),resolution=1,
                    relief=GROOVE,bd=2,width=10)
sizeValue.place(x=125,y=60)

minValueLabel= Label(root,text='Min Değer:',
                font=('times new roman',12,'italic'),
                width= 10,height=2, fg='black',bg='red',relief=GROOVE,bd=5)
minValueLabel.place(x=250,y=60)
minValue= Scale(root,from_=0,to=50,orient=HORIZONTAL,
                    font=('times new roman',14,'italic'),
                    relief=GROOVE,bd=2,width=10)
minValue.place(x=370,y=60)

maxValueLabel= Label(root,text='Max Değer:',
                font=('times new roman',12,'italic'),
                width= 10,height=2, fg='black',bg='red',relief=GROOVE,bd=5)
maxValueLabel.place(x=500,y=60)
maxValue= Scale(root,from_=0,to=200,resolution=1,orient=HORIZONTAL,
                    font=('times new roman',14,'italic'),
                    relief=GROOVE,bd=2,width=10)
maxValue.place(x=620,y=60)


#Hız ayarı yeri 
# Hız ayarı yeri
speedValueLabel = Label(root, text='Hız:', font=('times new roman', 12, 'italic'),
                        width=10, fg='black', bg='red', relief=GROOVE, bd=5)
speedValueLabel.place(x=400, y=0)
speedScale = Scale(root, from_=0.1, to=5.0, resolution=0.2, length=200, digits=2, orient=HORIZONTAL,
                   font=('times new roman', 14, 'italic'),
                   relief=GROOVE, bd=2, width=10)
speedScale.place(x=500, y=0)

#Grafik arayüzünün yeri 
canvas = Canvas(root, width=800, height=740, bg='White',relief=GROOVE, bd=5)
canvas.place(x=300,y=200)


root.mainloop()