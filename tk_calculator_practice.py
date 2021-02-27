from tkinter import *

window = Tk()
window.title("Asdafjboafyia")
window.iconbitmap("icono.ico")
window.geometry("310x600")
window.resizable(width = 0, height = 0)

#Panel

num_panel = StringVar()
panel = Entry(window, textvariable = num_panel)
panel.place(x = "0", y = "0", height = "100", width = "310")
panel.config(justify = "right", font = ("Arial", 60))


#Fila_One

def codebuton_7():
	num_panel.set(num_panel.get() + "7")

buton7 = Button(window, text = "7", font = ("Arial", 20), command = codebuton_7)
buton7.pack()
buton7.place(x = 5, y = 105)
buton7.config(padx = 30, pady = 30)

def codebuton_8():
	num_panel.set(num_panel.get() + "8")

buton8 = Button(window, text = "8", font = ("Arial", 20), command = codebuton_8)
buton8.pack()
buton8.place(x = 105, y = 105)
buton8.config(padx = 30, pady = 30)

def codebuton_9():
	num_panel.set(num_panel.get() + "9")

buton9 = Button(window, text = "9", font = ("Arial", 20), command = codebuton_9)
buton9.pack()
buton9.place(x = 205, y = 105)
buton9.config(padx = 30, pady = 30)

#Fila_Two

def codebuton_6():
	num_panel.set(num_panel.get() + "6")

buton6 = Button(window, text = "6", font = ("Arial", 20), command = codebuton_6)
buton6.pack()
buton6.place(x = 205, y = 225)
buton6.config(padx = 30, pady = 30)

def codebuton_5():
	num_panel.set(num_panel.get() + "5")

buton5 = Button(window, text = "5", font = ("Arial", 20), command = codebuton_5)
buton5.pack()
buton5.place(x = 105, y = 225)
buton5.config(padx = 30, pady = 30)

def codebuton_4():
	num_panel.set(num_panel.get() + "4")

buton4 = Button(window, text = "4", font = ("Arial", 20), command = codebuton_4)
buton4.pack()
buton4.place(x = 5, y = 225)
buton4.config(padx = 30, pady = 30)

#Fila_Three

def codebuton_3():
	num_panel.set(num_panel.get() + "3")

buton3 = Button(window, text = "3", font = ("Arial", 20), command = codebuton_3)
buton3.pack()
buton3.place(x = 205, y = 345)
buton3.config(padx = 30, pady = 30)

def codebuton_2():
	num_panel.set(num_panel.get() + "2")

buton2 = Button(window, text = "2", font = ("Arial", 20), command = codebuton_2)
buton2.pack()
buton2.place(x = 105, y = 345)
buton2.config(padx = 30, pady = 30)

def codebuton_1():
	num_panel.set(num_panel.get() + "1")

buton1 = Button(window, text = "1", font = ("Arial", 20), command = codebuton_1)
buton1.pack()
buton1.place(x = 5, y = 345)
buton1.config(padx = 30, pady = 30)

#Fila_Four_:

def codebuton_0():
	num_panel.set(num_panel.get() + "0")

buton0 = Button(window, text = "0", font = ("Arial", 20), command = codebuton_0)
buton0.pack()
buton0.place(x = 105, y = 465)
buton0.config(padx = 30, pady = 13)

#Fila_Four_Operations:

buton_suma = Button(window, text = "+", font = ("Arial", 15))
buton_suma.pack()
buton_suma.place(x = 5, y = 465)
buton_suma.config(padx = 35, pady =10)

buton_resta = Button(window, text = "-", font = ("Arial", 15))
buton_resta.pack()
buton_resta.place(x = 5, y = 530)
buton_resta.config(padx = 37, pady = 10)

buton_producto = Button(window, text = "x", font = ("Arial", 15))
buton_producto.pack()
buton_producto.place(x = 205, y = 465)
buton_producto.config(padx = 36, pady = 10)

buton_division = Button(window, text = "/", font = ("Arial", 15))
buton_division.pack()
buton_division.place(x = 205, y = 530)
buton_division.config(padx = 37, pady = 10)

buton_igual = Button(window, text = "=", font = ("Arial", 15))
buton_igual.pack()
buton_igual.place(x = 101, y = 550)
buton_igual.config(padx = 37, pady = 0)

window.mainloop()