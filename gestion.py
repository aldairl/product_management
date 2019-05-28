from tkinter import *

root = Tk()
root.title("Gestion de productos")
root.config(bg = "#107595")
root.geometry("500x600")

#---------------titulo----------------
logo = Frame(root, width = 500, height = 90)
logo.pack()
logo.config(bg = "#010059")
titulo = Label(logo, text = "Ingresar producto", bg  = "#010059" ,font = (36), fg = "#107595").place(x= 180, y = 30)


#--------------------formulario---------------------
formulario = Frame(root, width = 500, height =480)
formulario.config(bg = "#107595")
formulario.pack(fill = "y", expand = "True", pady = 20)
#formulario.pack()   


#-----codigo----------
codigo = Label(formulario, text = "Codigo:", font = (16), bg = "#107595", fg = "#010059" )
codigo.grid(row = 0, column = 0, sticky = "e", padx = 4, pady = 4)

codigoEntry = Entry(formulario)
codigoEntry.grid(row = 0, column = 1, padx = 4, pady = 4)
codigoEntry.config(font = (14))

#-----nombre----------
nombre = Label(formulario, text = "Nombre:", font = (16), bg = "#107595", fg = "#010059" )
nombre.grid(row = 1, column = 0, sticky = "e", padx = 4, pady = 4)

nombreEntry = Entry(formulario)
nombreEntry.grid(row = 1, column = 1, padx = 4, pady = 4)
nombreEntry.config(font = (14))

#-----Precio----------
nombre = Label(formulario, text = "Precio:", font = (16), bg = "#107595", fg = "#010059" )
nombre.grid(row = 2, column = 0, sticky = "e", padx = 4, pady = 4)

nombreEntry = Entry(formulario)
nombreEntry.grid(row = 2, column = 1, padx = 4, pady = 4)
nombreEntry.config(font = (14))

#-----Categoria----------
nombre = Label(formulario, text = "Categoría:", font = (16), bg = "#107595", fg = "#010059" )
nombre.grid(row = 3, column = 0, sticky = "e", padx = 4, pady = 4)

nombreEntry = Entry(formulario)
nombreEntry.grid(row = 3, column = 1, padx = 4, pady = 4)
nombreEntry.config(font = (14))

#-----------botones------------------

save = Button(formulario, text = "Guardar")
save.grid(row = 4, column = 1, padx = 4, pady = 8, sticky = "w")


root.mainloop()