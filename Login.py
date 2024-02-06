from tkinter import *
root = Tk()
root.title('Sistema ChocoBaha')
root.geometry('300x400')
root.config(padx=35, pady=35)

# Ventana de inicio de seión
texto = Label(root, text='Introduzca su usuario y contraseña', font=('Arial', 12)).grid(
    row=0, column=3)

Usuario = Entry(root, width=25)
Usuario.grid(row=1, column=3)

password = Entry(root, width=25, show='*')
password.grid(row=2, column=3)

# Botón y nueva ventana


def click_botón():
    ventana_nueva = Toplevel()
    ventana_nueva.title('Calculadora de Merma')
    ventana_nueva.geometry('400x500')
    ventana_nueva.config(padx=110, pady=60)
    texto2 = Label(ventana_nueva, text='Introduzca el peso',
                   font=('Arial', 14)).grid()
    Entrada_peso = Entry(ventana_nueva, text='Peso en Kg', width=10,
                         font=('arial, 14')).grid()
    Boton_2 = Button(ventana_nueva, text='Calcular',
                     command=click_botón).grid(pady=5)


botón1 = Button(root, text='Iniciar', padx=75, pady=10,
                command=click_botón).grid(row=3, column=3)


root.mainloop()

