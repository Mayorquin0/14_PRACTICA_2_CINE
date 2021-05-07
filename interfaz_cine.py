from tkinter import *
from tkinter import ttk
import cine_database

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

pelicula = StringVar()
hora= StringVar()
fecha = StringVar()
idiomas = StringVar()

def crear_sala():
    pelicula = entry_pelicula.get()
    hora = entry_hora.get()
    fecha = entry_fecha.get()
    idiomas = entry_idiomas.get()

    cine_db = cine_database.Mydatabase()
    cine_db.insert_db(pelicula, hora, fecha, idiomas)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=150)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender OPTIONS
frame_food = Frame(frame_options, width=350, height=450, bg="#F49090")
frame_food.place(x=25, y=30)
label_pelicula = Label(frame_food, 
              text="PELICULA",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#F49090")
label_pelicula.place(x=20, y=60)
entry_pelicula = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_pelicula.place(x=20, y=100)
label_hora= Label(frame_food, 
              text="HORA",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#F49090")
label_hora.place(x=20, y=130)
entry_hora = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"), show="*")
entry_hora.place(x=20, y=170)
label_fecha= Label(frame_food, 
              text="FECHA",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#F49090")
label_fecha.place(x=20, y=200)
entry_fecha = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_fecha.place(x=20, y=240)

label_idiomas = Label(frame_food, 
              text="IDIOMAs",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#F49090")
label_idiomas.place(x=20, y=280)
entry_idiomas = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_idiomas.place(x=20, y=320)

button_agregar = Button(frame_form, text="crear sala", 
                        font=("Calibri", "14", "bold"),
                        command= crear_sala)
button_register.place(x=20, y=440)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="Ticket",
              font=("Calibri", "14"))
title.place(x=320, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="Bienvenidos(as) al cine", 
              font=("Valentime", "24", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title,  
              font=("Modern Love Caps", "10"),
              justify=LEFT)
title2.place(x=25, y=50)

window.mainloop()