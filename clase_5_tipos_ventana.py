#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

"""
----------------------------
VENTANA DE APLICACION
----------------------------
"""
# class Aplicacion():
#     ''' Clase Aplicacion '''
#
#     # Declara una variable de clase para contar ventanas
#
#     ventana = 0
#
#     # Declara una variable de clase para usar en el
#     # cálculo de la posición de una ventana
#
#     posx_y = 0
#
#     def __init__(self):
#         ''' Construye ventana de aplicación '''
#
#         # Declara ventana de aplicación
#
#         self.raiz = Tk()
#
#         # Define dimensión de la ventana 300x200
#         # que se situará en la coordenada x=500,y=50
#
#         self.raiz.geometry('300x200+500+50')
#
#         self.raiz.resizable(0, 0)
#         self.raiz.title("Ventana de aplicación")
#
#         # Define botón 'Abrir' que se utilizará para
#         # abrir las ventanas de diálogo. El botón
#         # está vinculado con el método 'self.abrir'
#
#         boton = ttk.Button(self.raiz, text='Abrir', command=self.abrir)
#         boton.pack(side=BOTTOM, padx=20, pady=20)
#         self.raiz.mainloop()
#
#     def abrir(self):
#         ''' Construye una ventana de diálogo '''
#
#         # Define una nueva ventana de diálogo
#
#         self.dialogo = Toplevel()
#
#         # Incrementa en 1 el contador de ventanas
#
#         Aplicacion.ventana += 1
#
#         # Recalcula posición de la ventana
#
#         Aplicacion.posx_y += 50
#         tamypos = '500x100+' + str(Aplicacion.posx_y) + \
#                   '+' + str(Aplicacion.posx_y)
#         self.dialogo.geometry(tamypos)
#         #self.dialogo.resizable(0, 0)
#
#         # Obtiene identicador de la nueva ventana
#
#         ident = self.dialogo.winfo_id()
#
#         # Construye mensaje de la barra de título
#
#         titulo = str(Aplicacion.ventana) + ": " + str(ident)
#         self.dialogo.title(titulo)
#
#         # Define el botón 'Cerrar' que cuando sea presionado cerrará (destruirá) la ventana
#         # 'self.dialogo' llamando al método 'self.dialogo.destroy'
#
#         boton = ttk.Button(self.dialogo, text='Cerrar', command=self.dialogo.destroy)
#         boton.pack(side=BOTTOM, padx=20, pady=20)
#
#         # Cuando la ejecución del programa llega a este punto se utiliza el método wait_window() para
#         # esperar que la ventana 'self.dialogo' sea destruida.
#         # Mientras tanto se atiende a los eventos locales que se produzcan, por lo que otras partes de la
#         # aplicación seguirán funcionando con normalidad.
#         # Si hay código después de esta línea se ejecutará cuando la ventana 'self.dialogo' sea cerrada.
#
#         self.raiz.wait_window(self.dialogo)
#
#
# def main():
#     mi_app = Aplicacion()
#     return (0)
#
#
# if __name__ == '__main__':
#     main()


"""
----------------------------
VENTANA MODALES
----------------------------
"""


class Aplicacion():
    ventana = 0
    posx_y = 0

    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('300x200+500+50')
        self.raiz.resizable(0, 0)
        self.raiz.title("Ventana de aplicación")
        boton = ttk.Button(self.raiz, text='Abrir', command=self.abrir)
        boton.pack(side=BOTTOM, padx=20, pady=20)
        self.raiz.mainloop()

    def abrir(self):
        ''' Construye una ventana de diálogo '''

        self.dialogo = Toplevel()
        Aplicacion.ventana += 1
        Aplicacion.posx_y += 50
        tamypos = '200x100+' + str(Aplicacion.posx_y) + \
                  '+' + str(Aplicacion.posx_y)
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0, 0)
        ident = self.dialogo.winfo_id()
        titulo = str(Aplicacion.ventana) + ": " + str(ident)
        self.dialogo.title(titulo)
        boton = ttk.Button(self.dialogo, text='Cerrar', command=self.dialogo.destroy)
        boton.pack(side=BOTTOM, padx=20, pady=20)

        # Convierte la ventana 'self.dialogo' en
        # transitoria con respecto a su ventana maestra
        # 'self.raiz'.
        # Una ventana transitoria siempre se dibuja sobre
        # su maestra y se ocultará cuando la maestra sea
        # minimizada. Si el argumento 'master' es
        # omitido el valor, por defecto, será la ventana
        # madre.

        self.dialogo.transient(master=self.raiz)

        # El método grab_set() asegura que no haya eventos
        # de ratón o teclado que se envíen a otra ventana
        # diferente a 'self.dialogo'. Se utiliza para
        # crear una ventana de tipo modal que será
        # necesario cerrar para poder trabajar con otra
        # diferente. Con ello, también se impide que la
        # misma ventana se abra varias veces.

        self.dialogo.grab_set()
        self.raiz.wait_window(self.dialogo)


def main():
    mi_app = Aplicacion()
    return (0)


if __name__ == '__main__':
    main()

