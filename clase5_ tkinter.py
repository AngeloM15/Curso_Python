#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
--------------------------------
Primer Ejercicio
--------------------------------
"""

# Las dos líneas siguientes son necesaias para hacer
# compatible el interfaz Tkinter con los programas basados
# en versiones anteriores a la 8.5, con las más recientes.

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

# Define la ventana principal de la aplicación

raiz = Tk()

# Define las dimensiones de la ventana, que se ubicará en
# el centro de la pantalla. Si se omite esta línea la
# ventana se adaptará a los widgets que se coloquen en
# ella.

raiz.geometry('300x200') # anchura x altura

# Asigna un color de fondo a la ventana. Si se omite
# esta línea el fondo será gris

raiz.configure(bg = 'beige')

# Asigna un título a la ventana

raiz.title('Aplicación')

# Define un botón en la parte inferior de la ventana
# que cuando sea presionado hará que termine el programa.
# El primer parámetro indica el nombre de la ventana 'raiz'
# donde se ubicará el botón

ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)

# Después de definir la ventana principal y un widget botón
# la siguiente línea hará que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de
# que alguna persona interactúe con ella.

# Si la persona presiona sobre el botón Cerrar 'X', o bien,
# sobre el botón 'Salir' el programa llegará a su fin.

raiz.mainloop()


"""
----------------------------------------
Segundo Ejercicio Orientado a Objetos
----------------------------------------
"""
#
# from tkinter import *
# from tkinter import ttk
#
# # Crea una clase Python para definir el interfaz de usuario de
# # la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# # se ejecutará automáticamente el método __init__() qué
# # construye y muestra la ventana con todos sus widgets:
#
# class Aplicacion():
#     def __init__(self):
#         raiz = Tk()
#         raiz.geometry('300x200')
#         raiz.configure(bg = 'beige')
#         raiz.title('Aplicación')
#         ttk.Button(raiz, text='Salir',
#                    command=raiz.destroy).pack(side=BOTTOM)
#         raiz.mainloop()
#
# # Define la función main() que es en realidad la que indica
# # el comienzo del programa. Dentro de ella se crea el objeto
# # aplicación 'mi_app' basado en la clase 'Aplicación':
#
# def main():
#     mi_app = Aplicacion()
#     return 0
#
# # Mediante el atributo __name__ tenemos acceso al nombre de un
# # un módulo. Python utiliza este atributo cuando se ejecuta
# # un programa para conocer si el módulo es ejecutado de forma
# # independiente (en ese caso __name__ = '__main__') o es
# # importado:
#
# if __name__ == '__main__':
#     main()
#
#
#

"""
--------------------------------------------
Ejercicio 3: Obtener info de una ventana
--------------------------------------------
"""
#
# from tkinter import *
# from tkinter import ttk
#
#
# # La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# # nuevos widgets en el método constructor __init__(): Uno de
# # ellos es el botón 'Info'  que cuando sea presionado llamará
# # al método 'verinfo' para mostrar información en el otro
# # widget, una caja de texto: un evento ejecuta una acción:
#
# class Aplicacion():
#     def __init__(self):
#         # En el ejemplo se utiliza el prefijo 'self' para
#         # declarar algunas variables asociadas al objeto
#         # ('mi_app')  de la clase 'Aplicacion'. Su uso es
#         # imprescindible para que se pueda acceder a sus
#         # valores desde otros métodos:
#
#         self.raiz = Tk()
#         self.raiz.geometry('300x200')
#
#         # Impide que los bordes puedan desplazarse para
#         # ampliar o reducir el tamaño de la ventana 'self.raiz':
#
#         self.raiz.resizable(width=False, height=False)
#         self.raiz.title('Ver info')
#
#         # Define el widget Text 'self.tinfo ' en el que se
#         # pueden introducir varias líneas de texto:
#
#         self.tinfo = Text(self.raiz, width=40, height=10)
#
#         # Sitúa la caja de texto 'self.tinfo' en la parte
#         # superior de la ventana 'self.raiz':
#
#         self.tinfo.pack(side=TOP)
#
#         # Define el widget Button 'self.binfo' que llamará
#         # al metodo 'self.verinfo' cuando sea presionado
#
#         self.binfo = ttk.Button(self.raiz, text='Info',
#                                 command=self.verinfo)
#
#         # Coloca el botón 'self.binfo' debajo y a la izquierda
#         # del widget anterior
#
#         self.binfo.pack(side=LEFT)
#
#         # Define el botón 'self.bsalir'. En este caso
#         # cuando sea presionado, el método destruirá o
#         # terminará la aplicación-ventana 'self.raíz' con
#         # 'self.raiz.destroy'
#
#         self.bsalir = ttk.Button(self.raiz, text='Salir',
#                                  command=self.raiz.destroy)
#
#         # Coloca el botón 'self.bsalir' a la derecha del
#         # objeto anterior.
#
#         self.bsalir.pack(side=RIGHT)
#
#         # El foco de la aplicación se sitúa en el botón
#         # 'self.binfo' resaltando su borde. Si se presiona
#         # la barra espaciadora el botón que tiene el foco
#         # será pulsado. El foco puede cambiar de un widget
#         # a otro con la tecla tabulador [tab]
#
#         self.binfo.focus_set()
#         self.raiz.mainloop()
#
#     def verinfo(self):
#         # Borra el contenido que tenga en un momento dado
#         # la caja de texto
#
#         self.tinfo.delete("1.0", END)
#
#         # Obtiene información de la ventana 'self.raiz':
#
#         info1 = self.raiz.winfo_class()
#         info2 = self.raiz.winfo_geometry()
#         info3 = str(self.raiz.winfo_width())
#         info4 = str(self.raiz.winfo_height())
#         info5 = str(self.raiz.winfo_rootx())
#         info6 = str(self.raiz.winfo_rooty())
#         info7 = str(self.raiz.winfo_id())
#         info8 = self.raiz.winfo_name()
#         info9 = self.raiz.winfo_manager()
#
#         # Construye una cadena de texto con toda la
#         # información obtenida:
#
#         texto_info = "Clase de 'raiz': " + info1 + "\n"
#         texto_info += "Resolución y posición: " + info2 + "\n"
#         texto_info += "Anchura ventana: " + info3 + "\n"
#         texto_info += "Altura ventana: " + info4 + "\n"
#         texto_info += "Pos. Ventana X: " + info5 + "\n"
#         texto_info += "Pos. Ventana Y: " + info6 + "\n"
#         texto_info += "Id. de 'raiz': " + info7 + "\n"
#         texto_info += "Nombre objeto: " + info8 + "\n"
#         texto_info += "Gestor ventanas: " + info9 + "\n"
#
#         # Inserta la información en la caja de texto:
#
#         self.tinfo.insert("1.0", texto_info)
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


