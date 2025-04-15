import tkinter as tk
from tkinter import messagebox
import index
#USERS

usuarios=["admin"]
passwords=["1234"]

#COLORES
azul="lightblue"

def inicio():
    #VENTANA
    root=tk.Tk()
    root.title("Iniciar sesion")
    ancho_ventana=400
    alto_ventana=350
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    root.resizable(False,False)
    root.config(bg=azul)
    
    #TITULO
    labelTitulo=tk.Label(root,text="CRUISICORE")
    labelTitulo.config(font=("Arial",18),bg=azul)
    labelTitulo.place(x=120,y=50)

    #USUARIO
    labelSesion=tk.Label(root,text="USUARIO:")
    labelSesion.config(bg=azul)    
    labelSesion.place(x=115,y=150)
    entradaUsuario=tk.Entry(root)
    entradaUsuario.place(x=170,y=150)

    #PASSWORD
    labelPssw=tk.Label(root,text="PASSWORD:")
    labelPssw.config(bg=azul)
    labelPssw.place(x=100,y=200)
    entradaPssw=tk.Entry(root,show="*")
    entradaPssw.place(x=170,y=200)

    #BOTON CANCELAR
    botonCancelar=tk.Button(root,text="CANCELAR",command=root.destroy)
    botonCancelar.config(bg="red")
    botonCancelar.place(x=120,y=300)

    #BOTON INICIAR
    botonIniciar=tk.Button(root,text="INICIAR",command=lambda: comprobarUsuario(entradaUsuario,entradaPssw))
    botonIniciar.config(bg="green")
    botonIniciar.place(x=250,y=300)

    #INICIO
    root.mainloop()

def comprobarUsuario(user,pssw):
    usuario=str(user.get())
    password=str(pssw.get())
    if usuario not in usuarios or password not in passwords:
        messagebox.showerror("ERROR","Contraseña o usuario invalido")
    else:
        print("SI")

if __name__== "__main__":
    inicio()