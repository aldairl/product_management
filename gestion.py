from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Gestion de productos")

root.geometry("500x600")

#----------variables producto-------------

codigof = StringVar()
nombref = StringVar()
preciof = DoubleVar()
categoriaf = StringVar()
datos = []

#-----------Funciones---------------------

def conectarBD():
    
    # unique es para que no se pueda repertir
    try:

        conexion = sqlite3.connect("GestionProductos")
        miCursor = conexion.cursor()
        miCursor.execute('''
        CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CODIGO VARCHAR(10) UNIQUE,
        NOMBRE_ARTICULO VARCHAR(20),  
        PRECIO FLOAT,
        CATEGORIA VARCHAR (20)
            )
        ''')

        conexion.commit()
        conexion.close()

    
    except:

        print("Base de datos ya creada")

    messagebox.showinfo("Conectar a DB", "Conexión con exito")


#---------recuperar datos-----------

def getData():

    if codigof.get() != "" and nombref.get() != "" and preciof.get() != "" and categoriaf.get() != "":
        datos = []
        datos.append(codigof.get())
        datos.append(nombref.get())
        datos.append(preciof.get())
        datos.append(categoriaf.get())
        return datos
    
    else:
        return ""

#-------------Clear Data-----------------------------------

def clear():

    codigof.set("")
    nombref.set("")
    preciof.set("")
    categoriaf.set("")

#--------------insertar datos a Base de datos----------------
# 

def insertar():

    producto = getData()
    
    print("entrando", producto)
    if producto:

        try:
            
            conexion = sqlite3.connect("GestionProductos")
            miCursor = conexion.cursor()

            miCursor.execute("INSERT INTO PRODUCTOS VALUES (null,?,?,?,?)", producto)

            conexion.commit()
            clear()
            conexion.close()
            insertado.config(fg = "#010059")
            

        except:
            respuesta = messagebox.showinfo("dato existente", "ya existe un produto con la misma ID")
            
    else:
        messagebox.showinfo("Dato Vacio", "Es recomendable que ningun campo este vacio")
    
    

#---------------barra menu----------------

barraMenu = Menu(root)
barraMenu.config(bg = "#1a237e", fg = "#8c9eff")
root.config(bg = "#107595", menu = barraMenu)

menuArchivo = Menu(barraMenu, tearoff = 0)
menuArchivo.add_command(label = "cerrar")
menuArchivo.add_command(label = "conectar", command = conectarBD)

menuEdicion = Menu(barraMenu, tearoff = 0)
menuHerramientas = Menu(barraMenu, tearoff = 0)
menuAyuda = Menu(barraMenu, tearoff = 0)

barraMenu.add_cascade(label = "Archivo", menu = menuArchivo)
barraMenu.add_cascade(label = "Edición", menu = menuEdicion)
barraMenu.add_cascade(label = "Herramientas", menu = menuHerramientas)
barraMenu.add_cascade(label = "Ayuda", menu = menuAyuda)

#---------------titulo----------------
logo = Frame(root, width = 500, height = 90)
logo.pack()
logo.config(bg = "#010059")
titulo = Label(logo, text = "Ingresar producto", bg  = "#010059" ,font = (36), fg = "#107595").place(x= 180, y = 30)


#--------------------formulario Pesañas---------------------
formularioP = Frame(root, width = 500, height =480)
formularioP.config(bg = "#107595")
formularioP.pack(fill = "both", expand = "True")
#formulario.pack()   

#-----------*******pestañas*******-----------

menuPestanias = ttk.Notebook(formularioP)
menuPestanias.pack(fill = "both", expand = "yes")
pestaniaIngresar = ttk.Frame(menuPestanias)
pestaniaConsultar = ttk.Frame(menuPestanias)

menuPestanias.add(pestaniaIngresar, text = "Ingresar")
menuPestanias.add(pestaniaConsultar, text = "Consultar")

#-----------formulario---------------------------

formulario = Frame(pestaniaIngresar)
#formulario.config(bg = "#107595")
formulario.pack(fill = "y", expand = "yes")


#-----codigo----------
codigo = Label(formulario, text = "Codigo:", font = (16), fg = "#010059" )
codigo.grid(row = 0, column = 0, sticky = "e", padx = 4, pady = 4)

codigoEntry = Entry(formulario, textvariable = codigof)
codigoEntry.grid(row = 0, column = 1, padx = 4, pady = 4)
codigoEntry.config(font = (14))

#-----nombre----------
nombre = Label(formulario, text = "Nombre:", font = (16), fg = "#010059" )
nombre.grid(row = 1, column = 0, sticky = "e", padx = 4, pady = 4)

nombreEntry = Entry(formulario, textvariable = nombref)
nombreEntry.grid(row = 1, column = 1, padx = 4, pady = 4)
nombreEntry.config(font = (14))

#-----Precio----------
nombre = Label(formulario, text = "Precio:", font = (16), fg = "#010059" )
nombre.grid(row = 2, column = 0, sticky = "e", padx = 4, pady = 4)

precioEntry = Entry(formulario, textvariable = preciof )
precioEntry.grid(row = 2, column = 1, padx = 4, pady = 4)
precioEntry.config(font = (14))

#-----Categoria----------
nombre = Label(formulario, text = "Categoría:", font = (16), fg = "#010059" )
nombre.grid(row = 3, column = 0, sticky = "e", padx = 4, pady = 4)

categoriaEntry = Entry(formulario, textvariable = categoriaf)
categoriaEntry.grid(row = 3, column = 1, padx = 4, pady = 4)
categoriaEntry.config(font = (14))

#-----------botones------------------

save = Button(formulario, text = "Guardar", command = insertar)
save.grid(row = 4, column = 1, padx = 4, pady = 8, sticky = "w")

#------------etiqueta insertado-----------------------

insertado = Label(formulario, text = "Información insertada", font = (14), fg = "#f4eeed")

insertado.grid(row = 5, column = 1)

root.mainloop()