import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Mesa:
    color1="lightblue"
    color2="lightskyblue"
    color3="skyblue"
    color4="lightsteelblue"

    def __init__(self,mesas,numeroMesa,xd,yd):
        #DISEÑO
        anchoIcono=54
        largoIcono=45
        iconoOrdenar = Image.open("img/ordenar.png")
        iconoRedimensionado = iconoOrdenar.resize((anchoIcono, largoIcono))  
        self.iconoOrdenar= ImageTk.PhotoImage(iconoRedimensionado)

        iconoOrdenar = Image.open("img/cuenta.png")
        iconoRedimensionado = iconoOrdenar.resize((anchoIcono, largoIcono))  
        self.iconoCuenta= ImageTk.PhotoImage(iconoRedimensionado)

        iconoOrdenar = Image.open("img/reserva.png")
        iconoRedimensionado = iconoOrdenar.resize((anchoIcono, largoIcono))  
        self.iconoReserva= ImageTk.PhotoImage(iconoRedimensionado)
        
        self.frameMesa=tk.Frame(mesas,width=200,height=150,bd=10,relief="ridge",bg=self.color4)
        self.frameMesa.grid(row=xd,column=yd,padx=40,pady=60)

        self.labelNumeroMesa=tk.Label(self.frameMesa,text="MESA "+str(numeroMesa),bg=self.color4)
        self.labelNumeroMesa.place(x=70,y=40)

        self.frameBotones=tk.Frame(self.frameMesa,width=180,height=50)
        self.frameBotones.place(x=0,y=80)

        self.botonOrdenar=tk.Button(self.frameBotones,image=self.iconoOrdenar)#falta command
        self.botonOrdenar.grid(row=0,column=0)

        self.botonCuenta=tk.Button(self.frameBotones,image=self.iconoCuenta)#falta command
        self.botonCuenta.grid(row=0,column=1)
        
        self.botonReserva=tk.Button(self.frameBotones,image=self.iconoReserva)#falta command
        self.botonReserva.grid(row=0,column=2)