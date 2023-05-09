from tkinter import Tk, ttk, StringVar, Text


def gui():
    # configura la ventana
    window = Tk() # instancia la ventana
    window.title("RadioButtons") # Pone titulo
    window.geometry("200x150") # Le da tamaño
    window.resizable(0, 0) # no le permite cambiar el tamaño

    # Configuración de grid
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    # funcion reinciar
    def reiniciar():
        pelicula.set("")

    # Genera una leyenda y la ubica en el grid
    label_titulo_lista = ttk.Label(
        window, text="TU PELI FAVORITA:", foreground="black")
    label_titulo_lista.grid(column=0, row=0, sticky='w', columnspan=3, padx=5)

    # Variable pelicula seleccionada
    pelicula = StringVar()

    #listado de Radiobotton
    radio_botton_aladin = ttk.Radiobutton(window,text="Aladin",variable=pelicula,value="Aladin")
    radio_botton_aladin.grid(column=0,row=1,padx=5,pady=5, sticky='w')
    radio_botton_Hercules = ttk.Radiobutton(window, text="Hercules", variable=pelicula,value="Hercules")
    radio_botton_Hercules.grid(column=0, row=2, padx=5, pady=5, sticky='w')
    radio_botton_Tarzan = ttk.Radiobutton(window, text="Tarzan", variable=pelicula,value="Tarzan")
    radio_botton_Tarzan.grid(column=0, row=3, padx=5, pady=5, sticky='w')


    # Boton reiniciar
    style_button = ttk.Style()
    style_button.configure('btnReiniciar.TButton',
                           background='black')
    button_reiniciar = ttk.Button(window,text="REINICIAR",style='btnReiniciar.TButton',command = reiniciar)
    button_reiniciar.grid(column=2, row=8, sticky='s', pady=10)


    window.mainloop()


