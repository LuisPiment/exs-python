from tkinter import *
from ex006_1 import *

class Janela:
    def __init__(self,raiz1):

        self.placar1=0
        self.placar2=0

        self.fr1=Frame(raiz1,background=cinza1)
        self.fr1.pack()

        self.lb1=Label(self.fr1,text="Jogo de Par ou impar",font=fonte1,bg=cinza1,fg=azul2,pady=15)
        self.lb1.pack()

        self.lb2=Label(self.fr1,text=f"{'Player 1':<}" + f"{str(self.placar1):>5}" + f'{"x":^16}'+ f"{str(self.placar2):<4}" + f"{'Computador':<6}",font=fonte2,bg=cinza1,fg=azul_claro)
        self.lb2.pack()

        self.fr2=Frame(raiz1,bg=cinza1)
        self.fr2.pack()
        self.lb3=Label(self.fr2,text=f"{' P1':>}"+f"{'x':^3}"+f"{'CPU':<}",bg=cinza1,font=fonte4,pady=50)
        self.lb3.pack()

        self.fr3=Frame(raiz1,bg=cinza1)
        self.fr3.pack()

        self.escolha=StringVar()
        self.par=Radiobutton(self.fr3,text=f"{'Par'}",value="par",variable=self.escolha,bg=cinza1,font=fonte3,fg=vermelho,padx=30)
        self.par.pack(side=LEFT)

        self.impar=Radiobutton(self.fr3,text="Impar",value="impar",variable=self.escolha,bg=cinza1,font=fonte3,fg=vermelho,padx=70)
        self.impar.pack(side=LEFT)
      

        self.fr4=Frame(raiz1,bg=cinza1)
        self.fr4.pack()

        self.fr5=Frame(raiz1,bg=cinza1)
        self.fr5.pack()

        self.fr6=Frame(raiz1,bg=cinza1)
        self.fr6.pack()
        



        



raiz=Tk()
Janela(raiz)
raiz.geometry("900x800+550+150")
raiz.title("Jogo de para ou impar")
raiz["bg"]=cinza1
raiz.mainloop()
