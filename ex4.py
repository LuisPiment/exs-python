from tkinter import *


class Janela:
    def __init__(self,raiz1,raiz2):
        self.fr1=Frame(raiz1)
        self.fr1.pack()

        self.lb1=Label(self.fr1, text="Ola mundo")
        self.lb1.pack()

        self.bt1=Button(self.fr1,text="CLIQUE AQUI")
        self.bt1.pack()
        
        self.fr2=Frame(raiz2)
        self.fr2.pack()


raizz=Tk()
raiz=Tk()
Janela(raiz,raizz)
raiz.geometry("600x300+300+300")
raiz.mainloop()
raizz.mainloop()