from tkinter import *
from tkinter import messagebox
import pyttsx3,re

class Hablar:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry("500x350")
        self.raiz.title("Texto a voz")
        self.raiz.resizable(0,0)

        self.miFrame = Frame(self.raiz, width=1200, height=600, bg="bisque")
        self.miFrame.pack()

        self.textPantalla = Label(self.miFrame, text = "Ingrese el texto :", font = ("Angency FB",14))
        self.textPantalla.place(x=10,y=46)
        self.texto=StringVar()
        self.textCuadro = Entry(width=39, font = ("Angency FB",14),textvariable=self.texto).place(x=10,y=100)

        self.boton = Button(self.miFrame, text="Reproducir",width=10, height=1,anchor="center", command=self.validar,borderwidth=4)
        self.boton.config(cursor="hand2")
        self.boton ['bg'] = 'blue'
        self.boton ['fg'] = 'white'
        self.boton ['highlightbackground'] = 'black'
        self.boton ["relief"] = "groove"
        self.boton.place(x=205,y=200)

        self.raiz.mainloop()

    def voz(self,palabra):
            engine = pyttsx3.init()   
            voices=engine.getProperty('voices')
            engine.setProperty('voice','spanish-latin-am')
            engine.setProperty('rate', 150)   
            engine.setProperty('volume', 0.9)
            engine.say(palabra)
            engine.runAndWait()

    def validar(self):
        palabra = self.texto.get()
        validacion = re.match("^[A-z 0-9 \s]+$",palabra)
        if validacion is None:
            self.voz("Error")
            messagebox.showerror("Validación","Dato invalido")
            
        else: 
            self.voz(self.texto.get())
     
        