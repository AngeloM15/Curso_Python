#!/usr/bin/env python
# -*- coding: utf-8 -*-




""" METODO PACK"""
from tkinter import *
from tkinter import ttk, font
import getpass


# Gestor de geometría (pack)
#
# class Aplicacion():
#     def __init__(self):
#         self.raiz = Tk()
#         self.raiz.title("Acceso")
#
#         '''Cambia el formato de la fuente actual a negrita para resaltar las dos etiquetas que acompañan a las cajas
#         de entrada. (Para este cambio se ha importado el módulo 'font' al comienzo del programa):'''
#
#         fuente = font.Font(weight='bold')
#
#         '''Define las etiquetas que acompañan a las cajas de entrada y asigna el formato de fuente anterior:'''
#
#         self.etiq1 = ttk.Label(self.raiz, text="Usuario:", font=fuente)
#         self.etiq2 = ttk.Label(self.raiz, text="Contraseña:", font=fuente)
#
#         # Declara dos variables de tipo cadena para contener
#         # el usuario y la contraseña:
#
#         self.usuario = StringVar()
#         self.clave = StringVar()
#
#         # Realiza una lectura del nombre de usuario que
#         # inició sesión en el sistema y lo asigna a la
#         # variable 'self.usuario' (Para capturar esta
#         # información se ha importando el módulo getpass
#         # al comienzo del programa):
#
#         self.usuario.set(getpass.getuser())
#
#         '''Define dos cajas de entrada que aceptarán cadenas de una longitud máxima de 30 caracteres.
#
#         A la primera de ellas 'self.ctext1' que contendrá el nombre del usuario, se le asigna la variable
#         'self.usuario' a la opción 'textvariable'.
#         Cualquier valor que tome la variable durante la ejecución del programa quedará reflejada en la caja de entrada.
#         En la segunda caja de entrada, la de la contraseña, se hace lo mismo. Además, se establece la opción
#         'show' con un "*" (asterisco) para ocultar la escritura de las contraseñas:'''
#
#         self.ctext1 = ttk.Entry(self.raiz, textvariable=self.usuario, width=30)
#         self.ctext2 = ttk.Entry(self.raiz, textvariable=self.clave, width=30, show="*")
#         self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
#
#         '''Se definen dos botones con dos métodos:
#         El botón 'Aceptar' llamará al método 'self.aceptar' cuando sea presionado para validar la contraseña;
#         y el botón 'Cancelar' finalizará la aplicación si se llega a presionar:'''
#
#         self.boton1 = ttk.Button(self.raiz, text="Aceptar", command=self.aceptar)
#         self.boton2 = ttk.Button(self.raiz, text="Cancelar", command=quit)
#
#         '''Se definen las posiciones de los widgets dentro de la ventana. Todos los controles se van colocando
#         hacia el lado de arriba, excepto, los dos últimos, los botones, que se situarán debajo del último 'TOP':
#         el primer botón hacia el lado de la izquierda y el segundo a su derecha.
#
#         Los valores posibles para la opción 'side' son:
#         TOP (arriba),
#         BOTTOM (abajo)
#         LEFT (izquierda)
#         RIGHT (derecha)
#
#         Si se omite, el valor será TOP
#
#         La opción 'fill' se utiliza para indicar al gestor cómo expandir/reducir el widget si la ventana cambia
#         de tamaño.
#         Tiene tres posibles valores:
#         BOTH (Horizontal y Verticalmente),
#         X (Horizontalmente) e
#         Y (Verticalmente).
#         Funcionará si el valor de la opción 'expand' es True.
#
#         Por último, las opciones 'padx' y 'pady' se utilizan para añadir espacio extra externo horizontal y/o
#         vertical a los widgets para separarlos entre sí y de los bordes de la ventana.
#         Hay otras equivalentes que añaden espacio extra interno: 'ipàdx' y 'ipady':'''
#
#         self.etiq1.pack(side=TOP, fill=BOTH, expand=True,  padx=5, pady=5)
#         self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
#         self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
#         self.ctext2.pack(side=TOP, fill=X, expand=True,  padx=5, pady=5)
#         self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
#         self.boton1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
#         self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)
#
#         '''Cuando se inicia el programa se asigna el foco a la caja de entrada de la contraseña para que se
#         pueda empezar a escribir directamente:'''
#
#         self.ctext2.focus_set()
#
#         self.raiz.mainloop()
#
#     '''El método 'aceptar' se emplea para validar la contraseña introducida. Será llamado cuando se
#     presione el botón 'Aceptar'. Si la contraseña coincide con la cadena 'tkinter' se imprimirá
#     el mensaje 'Acceso permitido' y los valores aceptados. En caso contrario, se mostrará el
#     mensaje 'Acceso denegado' y el foco volverá al mismo lugar.'''
#
#     def aceptar(self):
#         if self.clave.get() == 'tkinter':
#             print("Acceso permitido")
#             print("Usuario:   ", self.ctext1.get())
#             print("Contraseña:", self.ctext2.get())
#         else:
#             print("Acceso denegado")
#
#             '''Se inicializa la variable 'self.clave' para que el widget 'self.ctext2' quede limpio.
#             Por último, se vuelve a asignar el foco a este widget para poder escribir una nueva
#             contraseña.'''
#
#             self.clave.set("")
#             self.ctext2.focus_set()
#
#
# def main():
#     mi_app = Aplicacion()
#     return 0
#
#
# if __name__ == '__main__':
#     main()
#





"""
----------------------------
METODO GRID
----------------------------
"""
#
# from tkinter import *
# from tkinter import ttk, font
# import getpass
#
#
# # Gestor de geometría (grid). Ventana no dimensionable
#
# class Aplicacion():
#     def __init__(self):
#         self.raiz = Tk()
#         self.raiz.title("Acceso")
#
#         # Establece que no se pueda modificar el tamaño de la
#         # ventana. El método resizable(0,0) es la forma abreviada
#         # de resizable(width=False,height=False).
#
#         self.raiz.resizable(0, 0)
#         fuente = font.Font(weight='bold')
#
#         # Define un widget de tipo 'Frame' (marco) que será el
#         # contenedor del resto de widgets. El marco se situará
#         # en la ventana 'self.raiz' ocupando toda su extensión.
#         # El marco se define con un borde de 2 píxeles y la
#         # opción 'relief' con el valor 'raised' (elevado) añade
#         # un efecto 3D a su borde.
#         # La opción 'relief' permite los siguientes valores:
#         # FLAT (llano), RAISED (elevado), SUNKEN (hundido),
#         # GROOVE (hendidura) y RIDGE (borde elevado).
#         # La opción 'padding' añade espacio extra interior para
#         # que los widgets no queden pegados al borde del marco.
#
#         self.marco = ttk.Frame(self.raiz, borderwidth=2, relief="raised", padding=(10, 10))
#
#         # Define el resto de widgets pero en este caso el primer
#         # paràmetro indica que se situarán en el widget del
#         # marco anterior 'self.marco'.
#
#         self.etiq1 = ttk.Label(self.marco, text="Usuario:", font=fuente, padding=(5, 5))
#         self.etiq2 = ttk.Label(self.marco, text="Contraseña:", font=fuente, padding=(5, 5))
#
#         # Define variables para las opciones 'textvariable' de
#         # cada caja de entrada 'ttk.Entry()'.
#
#         self.usuario = StringVar()
#         self.clave = StringVar()
#         self.usuario.set(getpass.getuser())
#         self.ctext1 = ttk.Entry(self.marco, textvariable=self.usuario, width=30)
#         self.ctext2 = ttk.Entry(self.marco, textvariable=self.clave, show="*", width=30)
#         self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
#         self.boton1 = ttk.Button(self.marco, text="Aceptar", padding=(5, 5), command=self.aceptar)
#         self.boton2 = ttk.Button(self.marco, text="Cancelar", padding=(5, 5), command=quit)
#
#         # Define la ubicación de cada widget en el grid.
#         # En este ejemplo en realidad hay dos grid (cuadrículas):
#         # Una cuadrícula de 1fx1c que se encuentra en la ventana
#         # que ocupará el Frame; y otra en el Frame de 5fx3c para
#         # el resto de controles.
#         # La primera fila y primera columna serán la número 0.
#         # La opción 'column' indica el número de columna y la
#         # opción 'row' indica el número de fila donde hay que
#         # colocar un widget.
#         # La opción 'columnspan' indica al gestor que el
#         # widget ocupará en total un número determinado de
#         # columnas. Las cajas para entradas 'self.ctext1' y
#         # 'self.ctext2' ocuparán dos columnas y la barra
#         # de separación 'self.separ1' tres.
#
#         self.marco.grid(column=0, row=0)
#         self.etiq1.grid(column=0, row=0)
#         self.ctext1.grid(column=1, row=0, columnspan=2)
#         self.etiq2.grid(column=0, row=1)
#         self.ctext2.grid(column=1, row=1, columnspan=2)
#         self.separ1.grid(column=0, row=3, columnspan=3)
#         self.boton1.grid(column=1, row=4)
#         self.boton2.grid(column=2, row=4)
#
#         # Establece el foco en la caja de entrada de la
#         # contraseña.
#
#         self.ctext2.focus_set()
#         self.raiz.mainloop()
#
#     def aceptar(self):
#         if self.clave.get() == 'tkinter':
#             print("Acceso permitido")
#             print("Usuario:   ", self.ctext1.get())
#             print("Contraseña:", self.ctext2.get())
#         else:
#             print("Acceso denegado")
#             self.clave.set("")
#             self.ctext2.focus_set()
#
#
# def main():
#     mi_app = Aplicacion()
#     return 0
#
#
# if __name__ == '__main__':
#     main()
#
#



"""
----------------------------
METODO PLACE
----------------------------
"""

from tkinter import *
from tkinter import ttk, font
import getpass


# Gestor de geometría (place)

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()

        # Define la dimensión de la ventana

        self.raiz.geometry("430x200")

        # Establece que no se pueda cambiar el tamaño de la
        # ventana

        self.raiz.resizable(0, 0)
        self.raiz.title("Acceso")
        self.fuente = font.Font(weight='bold')
        self.etiq1 = ttk.Label(self.raiz, text="Usuario:", font=self.fuente)
        self.etiq2 = ttk.Label(self.raiz, text="Contraseña:", font=self.fuente)

        # Declara una variable de cadena que se asigna a
        # la opción 'textvariable' de un widget 'Label' para
        # mostrar mensajes en la ventana. Se asigna el color
        # azul a la opción 'foreground' para el mensaje.

        self.mensa = StringVar()
        self.etiq3 = ttk.Label(self.raiz, textvariable=self.mensa, font=self.fuente, foreground='blue')

        self.usuario = StringVar()
        self.clave = StringVar()
        self.usuario.set(getpass.getuser())
        self.ctext1 = ttk.Entry(self.raiz, textvariable=self.usuario, width=30)
        self.ctext2 = ttk.Entry(self.raiz, textvariable=self.clave, width=30, show="*")
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.raiz, text="Aceptar", padding=(5, 5), command=self.aceptar)
        self.boton2 = ttk.Button(self.raiz, text="Cancelar", padding=(5, 5), command=quit)

        # Se definen las ubicaciones de los widgets en la
        # ventana asignando los valores de las opciones 'x' e 'y'
        # en píxeles.

        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=80)
        self.etiq3.place(x=150, y=120)
        self.ctext1.place(x=150, y=42)
        self.ctext2.place(x=150, y=82)
        self.separ1.place(x=5, y=145, bordermode=OUTSIDE,
                          height=10, width=420)
        self.boton1.place(x=170, y=160)
        self.boton2.place(x=290, y=160)
        self.ctext2.focus_set()

        # El método 'bind()' asocia el evento de 'hacer clic
        # con el botón izquierdo del ratón en la caja de entrada
        # de la contraseña' expresado con '<button-1>' con el
        # método 'self.borrar_mensa' que borra el mensaje y la
        # contraseña y devuelve el foco al mismo control.
        # Otros ejemplos de acciones que se pueden capturar:
        # <double-button-1>, <buttonrelease-1>, <enter>, <leave>,
        # <focusin>, <focusout>, <return>, <shift-up>, <key-f10>,
        # <key-space>, <key-print>, <keypress-h>, etc.

        self.ctext2.bind('<button-1>', self.borrar_mensa)
        self.raiz.mainloop()

    # Declara método para validar la contraseña y mostrar
    # un mensaje en la propia ventana, utilizando la etiqueta
    # 'self.mensa'. Cuando la contraseña es correcta se
    # asigna el color azul a la etiqueta 'self.etiq3' y
    # cuando es incorrecta el color rojo. Para ello. se emplea
    # el método 'configure()' que permite cambiar los valores
    # de las opciones de los widgets.

    def aceptar(self):
        if self.clave.get() == 'tkinter':
            self.etiq3.configure(foreground='blue')
            self.mensa.set("Acceso permitido")
        else:
            self.etiq3.configure(foreground='red')
            self.mensa.set("Acceso denegado")

    # Declara un método para borrar el mensaje anterior y
    # la caja de entrada de la contraseña

    def borrar_mensa(self, evento):
        self.clave.set("")
        self.mensa.set("")


def main():
    mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()