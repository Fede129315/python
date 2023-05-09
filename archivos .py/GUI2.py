import tkinter as tk # importa la libreria
#funcion reiniciar

def gui2():

# INSTANCIA LA VENTANA TK().
    ventana = tk.Tk()
    ventana.title("Lista de prueba en python")
    ventana.geometry("800x350+350+100") #los mas indican las cordenada donde aparece la ventana
    ventana.resizable(width=False,height=False)
    ventana.configure(background="lightgrey")



# IMPLEMENTAR WIDGETS - ROTULO
    rotulo = tk.Label(ventana,
        text="LISTA DE RADIOBOTTON\n CON PELÍCULAS",
        font="arial 20 bold",
        bg="grey",
        fg="black",
        padx=20,
        pady=20,
        anchor="center",
        relief="raised",
        border=5)
    rotulo.pack()
# IMPLEMENTAR WIDGETS - FRAME PARA LISTA CON SU ROTULO Y SUS RADIOBUTTONS
    cuadro1 = tk.Frame(ventana,
        bg="lightblue")
    cuadro1.pack(padx=20,pady=20)

    rotulo_peliculas = tk.Label(cuadro1,text="PELICULAS",
        fg="black",
        bg="lightblue",
        font="arial 12 bold")
    rotulo_peliculas.pack(side=tk.LEFT,padx=20,pady=20)

## FUNCION RESET
    def reiniciar():
        pelicula.set(0)

## VARIABLE PELICULA SELECCIONADA
    pelicula = tk.IntVar()

## LISTADO RADIOBUTTON CON LAS OPCIONES
    radio_botton_aladin = tk.Radiobutton(cuadro1,text="Aladin",variable=pelicula,value=1)
    radio_botton_aladin.pack(side=tk.LEFT,padx=20,pady=20)
    radio_botton_Hercules = tk.Radiobutton(cuadro1, text="Hercules", variable=pelicula,value=2)
    radio_botton_Hercules.pack(side=tk.LEFT,padx=20,pady=20)
    radio_botton_Tarzan = tk.Radiobutton(cuadro1, text="Tarzan", variable=pelicula,value=3)
    radio_botton_Tarzan.pack(side=tk.LEFT,padx=20,pady=20)
    radio_botton_Tarzan = tk.Radiobutton(cuadro1, text="Shrek", variable=pelicula,value=4)
    radio_botton_Tarzan.pack(side=tk.LEFT,padx=20,pady=20)



# IMPLEMENTAR WIDGETS - BUTTON
    botonreinicio = tk.Button(ventana,
        text="REINICIAR",
        font="arial 10 bold",
        bg="grey",
        fg="black",
        padx=20,
        pady=20,
        anchor=tk.SE,
        relief="raised",
        border=5,
        command=reiniciar)
    botonreinicio.pack(pady=20,padx=20)


# BUCLE PRINCIPAL DEL PROGRAMA
    ventana.mainloop()
