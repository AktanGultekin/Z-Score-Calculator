import tkinter as tk
from tkinter import *
import math

def calculate():
    mean = float(value1.get())
    std = float(value2.get())
    x = float(value3.get())
    result = float((x-mean)/std)
    rounded_result = round(result, 2)
    value4.delete(0, END)
    value4.insert(0, rounded_result)
    

main = tk.Tk()
main.geometry("320x260")
main.title("Z Score Calculator")


label1 = tk.Label(text = "Population Mean Value: ")
label1.pack(pady= 5)

value1 = tk.Entry()
value1.pack()

label2 = tk.Label(text="Population Standart Deviation: ")
label2.pack(pady= 5)

value2 = tk.Entry()
value2.pack()

label3 = tk.Label(text="X Value: ")
label3.pack(pady= 5)

value3 = tk.Entry()
value3.pack()

label4 = tk.Label(text = "Z-Score: ")
label4.pack(pady= 5)

value4 = tk.Entry()
value4.pack()

button = tk.Button(text="Calculate", command= calculate)
button.pack(pady= 10)



main.mainloop()