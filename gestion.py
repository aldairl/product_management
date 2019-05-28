from tkinter import *

root = Tk()
root.title("Gestion de productos")
root.config(bg = "#fcf594")
root.geometry("500x600")

#---------------titulo----------------
logo = Frame(root, width = 500, height = 90)
logo.pack()
logo.config(bg = "#010059")
titulo = Label(logo, text = "Ingresar producto", bg  = "#010059" ,font = (36), fg = "#107595").place(x= 180, y = 30)


#--------------------formulario---------------------
formulario = Frame(root, width = 500, height =480)
formulario.config(bg = "#107595")
formulario.pack()




root.mainloop()