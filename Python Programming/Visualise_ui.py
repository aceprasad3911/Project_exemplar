# option 3
import csv
import matplotlib.pyplot as plt
import tkinter as tk
from datahandler import data
components = {}


# create the window
def visualise():
    createwindow()


# window execution
def createwindow():
    window = windowcon()
    component(window)
    window.mainloop()


# window configuration
def windowcon():
    window = tk.Tk()
    window.geometry("900x150")
    window.title("Summary")
    window.config(bg="#252394", padx=5, pady=5)
    window.columnconfigure(0, weight=3)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=3)
    window.rowconfigure(0, weight=3)
    window.rowconfigure(1, weight=3)
    window.rowconfigure(2, weight=3)
    return window


# label config
def label(window):
    label1 = tk.Label(window)
    label1.config(text="Select an option:", font=("Times New Roman", 12))
    label1.grid(row=0, column=1)
    components["label1"] = label1


# button 1 piechart config
def buttonone(window):
    button1 = tk.Button(window)
    button1.config(text="Pie Chart No. Of Employees", font=("Harlow Solid Italic", 16))
    button1.grid(row=2, column=0)
    button1.bind("<ButtonRelease-1>", piechart)
    components["button1"] = button1


# button 2 configuraton histogram
def buttontwo(window):
    button2 = tk.Button(window)
    button2.config(text="Histogram Distance From Home", font=("Harlow Solid Italic", 16))
    button2.grid(row=2, column=2)
    button2.bind("<ButtonRelease-1>", histogram)
    components["button2"] = button2


# adds components
def component(window):
    buttonone(window)
    buttontwo(window)
    label(window)


# piechart config
def piechart(event):
    reader = csv.DictReader(data)
    rec = list(reader)
    mat = [row for row in rec if row['Department'] == 'Maternity']
    card = [row for row in rec if row['Department'] == 'Cardiology']
    neu = [row for row in rec if row['Department'] == 'Neurology']

    labels = (f'Cardiology {len(card)}', f'Maternity {len(mat)}', f'Neurology {len(neu)}')
    sizes = [len(card), len(mat), len(neu)]
    plt.title("Employees per Department")
    plt.pie(sizes, labels=labels)
    plt.show()


# histogram config
def histogram(event):
    reader = csv.DictReader(data)
    rec = list(reader)

    dist = [int(record['DistanceFromHome']) for record in rec]
    numemp = {}
    for value in dist:
        numemp[value] = numemp.get(value, 0) + 1

    x = list(numemp.keys())
    y = list(numemp.values())

    plt.title("Distances From Home")
    plt.xlabel("Distances / m")
    plt.ylabel("Num Of Employees")
    plt.bar(x, y)
    plt.show()
