import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from conexion import *

class Cuisinecore:
    color1="lightblue"
    color2="lightskyblue"
    color3="skyblue"

    def salir(self):
        confirmacion=messagebox.askquestion("CONFIRMAR","Estas seguro que deseas salir?")

        if confirmacion == "yes":
            self.root.destroy()#cambio
        else:
            return
        
    def agregarProducto(self):
        try:
            nombre=self.entryNombreProducto.get()
            costo=float(self.entryCostoProducto.get())
            tipo=self.entryTipo.get()
            porcion=int(self.entryPorcion.get())
            if not nombre or not costo or not tipo or not porcion:
                messagebox.showerror("ERROR","Ingresa una datos validos")
                return
        except:
            messagebox.showerror("ERROR","Algo salio mal :/")
            return
        conn,cursor = conexion()

        if conn and cursor:
            try:
                cursor.execute("INSERT INTO producto (nombre, costo,tipo,porcion) VALUES (%s, %s, %s,%s) RETURNING clave", 
                    (nombre, costo, tipo,porcion))
                conn.commit()
                messagebox.showinfo("Exito", "Empleado agregado correctamente")
                id=cursor.fetchone()[0]
                self.treeviewProductos.insert("", "end", values=(nombre, costo, tipo,porcion,id))
                self.entryNombreProducto.delete(0, tk.END)
                self.entryCostoProducto.delete(0, tk.END)
                self.entryTipo.set('')
                self.entryPorcion.delete(0, tk.END)

            except psycopg2.Error as e:
                messagebox.showerror("Error","Error al consultar la base de datos: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Error","No se pudo conectar a la base de datos")

    def agregarEmpleado(self):
        try:
            nombre=self.entryNombreEmpleado.get()
            pssw=self.entryContraseña.get()
            psswC=self.entryConfirmar.get()
            edad=int(self.entryEdad.get())
            if not pssw or not psswC or not nombre or not edad:
                messagebox.showerror("ERROR","Ingresa una datos validos")
                return
            if pssw != psswC:
                messagebox.showerror("ERROR","La contraseña no coincide")
                return
           
        except:
            messagebox.showerror("ERROR","Algo salio mal :/")
            return
        conn,cursor = conexion()

        if conn and cursor:
            try:
                cursor.execute("INSERT INTO empleado (nombre, contraseña, edad) VALUES (%s, %s, %s) RETURNING id", 
                    (nombre, pssw, edad))
                conn.commit()
                messagebox.showinfo("Exito", "Empleado agregado correctamente")
                id=cursor.fetchone()[0]
                self.treeviewEmpleados.insert("", "end", values=(nombre, edad, id))
                self.entryNombreEmpleado.delete(0, tk.END)
                self.entryContraseña.delete(0, tk.END)
                self.entryConfirmar.delete(0, tk.END)
                self.entryEdad.delete(0, tk.END)
            except psycopg2.Error as e:
                messagebox.showerror("Error","Error al consultar la base de datos: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Error","No se pudo conectar a la base de datos")

    def eliminarProducto(self):
        seleccion=self.treeviewProductos.selection()
        if not seleccion:
            messagebox.showerror("Error","No hay ninguna seleccion para eliminar")
            return
        
        conn,cursor = conexion()
        claveProducto=""
        if conn and cursor:
            try:
                for item in seleccion:
                    valores=self.treeviewProductos.item(item,"values")
                    claveProducto=valores[4]
                cursor.execute("DELETE from producto WHERE clave = %s",(claveProducto,))
                conn.commit()
                messagebox.showinfo("Exito", "Producto eliminado correctamente")
                self.treeviewProductos.delete(*self.treeviewProductos.get_children())
                self.cargar_datosProductos()
                
            except psycopg2.Error as e:
                messagebox.showerror("Error","Error al consultar la base de datos: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Error","No se pudo conectar a la base de datos")
    def eliminarEmpleado(self):
        seleccion=self.treeviewEmpleados.selection()
        if not seleccion:
            messagebox.showerror("Error","No hay ninguna seleccion para eliminar")
            return
        
        conn,cursor = conexion()
        claveEmpleado=""
        if conn and cursor:
            try:
                for item in seleccion:
                    valores=self.treeviewEmpleados.item(item,"values")
                    claveEmpleado=valores[2]
                cursor.execute("DELETE from empleado WHERE id = %s",(claveEmpleado,))
                conn.commit()
                messagebox.showinfo("Exito", "Producto eliminado correctamente")
                self.treeviewEmpleados.delete(*self.treeviewEmpleados.get_children())
                self.cargar_datosEmpleados()
                
            except psycopg2.Error as e:
                messagebox.showerror("Error","Error al consultar la base de datos: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Error","No se pudo conectar a la base de datos")
        
    def cargar_datosProductos(self):
        # Conectar
        conn, cursor = conexion()

        if conn and cursor:
            try:
                cursor.execute("SELECT nombre, costo,tipo,porcion, clave FROM producto") 
                rows = cursor.fetchall()

                # Insertar
                for row in rows:
                    self.treeviewProductos.insert("", "end", text=row[1], values=(row[0], row[1], row[2],row[3],row[4]))

            except psycopg2.Error as e:
                messagebox.showerror("Error","Error al consultar la base de datos: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Error","No se pudo conectar a la base de datos")

    def cargar_datosEmpleados(self):
        # Conectar
        conn, cursor = conexion()

        if conn and cursor:
            try:
                cursor.execute("SELECT nombre, edad, id FROM empleado") 
                rows = cursor.fetchall()

                # Insertar
                for row in rows:
                    self.treeviewEmpleados.insert("", "end", text=row[1], values=(row[0], row[1], row[2]))

            except psycopg2.Error as e:
                messagebox.showerror("Error","Error al consultar la base de datos: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Error","No se pudo conectar a la base de datos")
        
    def __init__(self):
        
        #VENTANA
        self.root=tk.Tk()
        self.root.title("CUISINECORE")
        self.root.attributes("-fullscreen", True)
        self.root.config(bg=self.color2)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        #NOMBRE
        self.frameBienvenida=tk.Frame(self.root,bg=self.color1,height=100)
        self.frameBienvenida.pack(fill="both")
        self.labelNombre=tk.Label(self.frameBienvenida,text="Bienvenid@        CUISINECORE",font=("ARIAL",24))      
        self.labelNombre.config(bg=self.color1)
        self.labelNombre.pack(padx=5,pady=5)

        #BOTON SALIR
        self.botonSalir=tk.Button(self.frameBienvenida,text="SALIR",font=("ARIAL",15),command=self.salir)
        self.botonSalir.pack(side="right",padx=15)
        self.botonSalir.config(bg="red")

        #SUBMENUS
        self.tabMenu=ttk.Notebook(self.root,height=700)
        #self.tabMenu.place(x=50,y=125,height=700,width=1450)
        self.tabMenu.pack(fill="both",padx=50,pady=80)

        #Pestaña1 PRODUCTO
        producto=tk.Frame(self.tabMenu)
        producto.config(bg=self.color3)
        self.labelAgregarProducto = tk.Label(producto, text="Agregar un producto:", font=("Helvatica", 14,"bold"))
        self.labelAgregarProducto.config(bg=self.color3)
        self.labelAgregarProducto.place(y=25,x=605)

        self.labelNombreProducto=tk.Label(producto,text="Nombre del producto: ",font=("Times", 12))
        self.labelNombreProducto.config(bg="lightblue")
        self.labelNombreProducto.place(x=100,y=100)
        self.entryNombreProducto=tk.Entry(producto)
        self.entryNombreProducto.place(x=275,y=100)

        self.labelCostoProducto=tk.Label(producto,text="Costo del producto: ",font=("Times", 12))
        self.labelCostoProducto.config(bg="lightblue")
        self.labelCostoProducto.place(x=100,y=150)
        self.entryCostoProducto=tk.Entry(producto)
        self.entryCostoProducto.place(x=275,y=150)

        self.labelTipo=tk.Label(producto,text="Tipo de producto: ",font=("Times", 12))
        self.labelTipo.config(bg="lightblue")
        self.labelTipo.place(x=100,y=200)
        self.entryTipo=ttk.Combobox(producto,state="readonly",values=("Entrada","Platillo","Bebida"),width=17)
        self.entryTipo.place(x=275,y=200)

        self.labelPorcion=tk.Label(producto,text="Porcion del producto: ",font=("Times", 12))
        self.labelPorcion.config(bg="lightblue")
        self.labelPorcion.place(x=100,y=250)
        self.entryPorcion=tk.Entry(producto)
        self.entryPorcion.place(x=275,y=250)

        self.botonAgregarProducto=tk.Button(producto,text="AGREGAR",command=self.agregarProducto)
        self.botonAgregarProducto.config(bg="lightgreen")
        self.botonAgregarProducto.place(x=215,y=300)

        self.treeviewProductos = ttk.Treeview(producto, columns=("Nombre", "Precio", "Tipo","Porcion","Clave"),show="headings",height=20)
        self.treeviewProductos.place(x=420,y=100)

        self.treeviewProductos.column("Nombre", width=300,anchor="center")
        self.treeviewProductos.column("Precio", width=100,anchor="center")
        self.treeviewProductos.column("Tipo", width=200,anchor="center")
        self.treeviewProductos.column("Porcion", width=200,anchor="center")
        self.treeviewProductos.column("Clave", width=200,anchor="center")

        self.treeviewProductos.heading("Nombre", text="Nombre")  
        self.treeviewProductos.heading("Precio", text="Precio")
        self.treeviewProductos.heading("Tipo", text="Tipo")
        self.treeviewProductos.heading("Porcion", text="Porcion")
        self.treeviewProductos.heading("Clave", text="Clave")

        self.botonEliminarProducto=tk.Button(producto,text="ELIMINAR SELECCION",command=self.eliminarProducto)
        self.botonEliminarProducto.config(bg="red")
        self.botonEliminarProducto.place(x=915,y=550)
        
        self.treeviewProductos.delete(*self.treeviewProductos.get_children())
        self.cargar_datosProductos()

        #Pestaña2 MESAS
        mesas=tk.Frame(self.tabMenu)
        mesas.config(bg=self.color3)
        self.labelMesa = tk.Label(mesas, text="Modificar mesa:", font=("Helvatica", 14,"bold"))
        self.labelMesa.config(bg=self.color3)
        self.labelMesa.place(y=25,x=605)

        #Pestaña3 EMPLEADOS
        empleados=tk.Frame(self.tabMenu)
        empleados.config(bg=self.color3)
        self.labelAgregarEmpleado = tk.Label(empleados, text="Agregar un empleado:", font=("Helvatica", 14,"bold"))
        self.labelAgregarEmpleado.config(bg=self.color3)
        self.labelAgregarEmpleado.place(y=25,x=605)

        self.labelNombreEmpleado=tk.Label(empleados,text="Nombre del empleado: ",font=("Times", 12))
        self.labelNombreEmpleado.config(bg="lightblue")
        self.labelNombreEmpleado.place(x=250,y=100)
        self.entryNombreEmpleado=tk.Entry(empleados)
        self.entryNombreEmpleado.place(x=425,y=100)

        self.labelContraseña=tk.Label(empleados,text="Contraseña del empleado: ",font=("Times", 12))
        self.labelContraseña.config(bg="lightblue")
        self.labelContraseña.place(x=250,y=150)
        self.entryContraseña=tk.Entry(empleados,show="*")
        self.entryContraseña.place(x=425,y=150)

        self.labelConfirmar=tk.Label(empleados,text="Confirmar contraseña: ",font=("Times", 12))
        self.labelConfirmar.config(bg="lightblue")
        self.labelConfirmar.place(x=250,y=200)
        self.entryConfirmar=tk.Entry(empleados,show="*")
        self.entryConfirmar.place(x=425,y=200)

        self.labelEdad=tk.Label(empleados,text="Edad del empleado: ",font=("Times", 12))
        self.labelEdad.config(bg="lightblue")
        self.labelEdad.place(x=250,y=250)
        self.entryEdad=tk.Entry(empleados)
        self.entryEdad.place(x=425,y=250)

        self.botonAgregarEmpleado=tk.Button(empleados,text="AGREGAR",command=self.agregarEmpleado)
        self.botonAgregarEmpleado.config(bg="lightgreen")
        self.botonAgregarEmpleado.place(x=370,y=300)

        self.treeviewEmpleados = ttk.Treeview(empleados, columns=("Nombre", "Edad", "ID"),show="headings",height=20)
        self.treeviewEmpleados.place(x=620,y=100)

        self.treeviewEmpleados.column("Nombre", width=200,anchor="center")
        self.treeviewEmpleados.column("Edad", width=300,anchor="center")
        self.treeviewEmpleados.column("ID", width=200,anchor="center")

        self.treeviewEmpleados.heading("Nombre", text="Nombre")  
        self.treeviewEmpleados.heading("Edad", text="Edad")
        self.treeviewEmpleados.heading("ID", text="ID")

        self.botonEliminarEmpleado=tk.Button(empleados,text="ELIMINAR SELECCION",command=self.eliminarEmpleado)
        self.botonEliminarEmpleado.config(bg="red")
        self.botonEliminarEmpleado.place(x=915,y=550)
        
        self.treeviewEmpleados.delete(*self.treeviewEmpleados.get_children())
        self.cargar_datosEmpleados()
        
        #NOMBRES SUBMENUS
        self.tabMenu.add(producto, text="Productos")
        self.tabMenu.add(mesas, text="Mesas")
        self.tabMenu.add(empleados, text="Empleados")

        #INICIO
        self.root.mainloop()

if __name__== "__main__":
    Cuisinecore()