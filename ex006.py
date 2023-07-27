from tkinter import *
from ex006_1 import *
from random import randint

class Janela:
    
    
    def __init__(self,raiz1):
        self.cpu5=0
        self.p15=0

        self.fr1=Frame(raiz1,background=cinza1)
        self.fr1.pack()

        self.lb1=Label(self.fr1,text="Jogo de Par ou impar",font=fonte1,bg=cinza1,fg=azul2,pady=15)
        self.lb1.pack()

        self.lb3=Label(self.fr1,text=f"{' '}",font=fonte2,bg=cinza1,fg="blue")
        self.lb3.pack()

        self.lb2=Label(self.fr1,text=f"{'Player 1':<}" + f"{self.p15:>5}" + f'{"x":^16}'+ f"{self.cpu5:<4}" + f"{'Computador':<6}",font=fonte2,bg=cinza1,fg=azul_claro)
        self.lb2.pack()

        self.fr2=Frame(raiz1,bg=cinza1)
        self.fr2.pack()

        self.lb6=Label(self.fr2,text=f"{' P1':>}"+f"{'x':^3}"+f"{'CPU':<}",bg=cinza1,font=fonte4,pady=50)
        self.lb6.pack()

        self.fr3=Frame(raiz1,bg=cinza1)
        self.fr3.pack()

        self.escolha=StringVar()

        self.par=Radiobutton(self.fr3,text=f"{'Par'}",value="par",variable=self.escolha,bg=cinza1,font=fonte3,fg="purple",padx=30)
        self.par.pack(side=LEFT)

        self.impar=Radiobutton(self.fr3,text="Impar",value="impar",variable=self.escolha,bg=cinza1,font=fonte3,fg="purple",padx=70)
        self.impar.pack(side=LEFT)
        
        self.fr4=Frame(raiz1,bg=cinza1)
        self.fr4.pack()

        self.lb4=Label(self.fr4,text="Digite um numero de 1 a 10 :",font=fonte1,bg=cinza1)
        self.lb4.pack(side=LEFT)
        
        self.num=Entry(self.fr4,width=2,font=fonte1)
        self.num.pack()

        self.fr5=Frame(raiz1,bg=cinza1)
        self.fr5.pack()

        self.jogar10=Button(self.fr5,text="JOGAR    ",bg=cinza2,font=fonte1,command=self.jogar)
        self.jogar10.bind("<Return>",self.jogar2)
        self.jogar10.pack() 

        self.resetar=Button(self.fr5,text="Resetar",bg=cinza2,font=fonte1,command=self.reset)
        self.resetar.bind("<Return>",self.reset2)
        self.resetar.pack()


        self.fr6=Frame(raiz1,bg=cinza1)
        self.fr6.pack()
        self.lb5=Label(self.fr6,text=" ",fg="red",bg=cinza1,font=fonte2)
        self.lb5.pack()
    def reset(self):
        self.cpu5=0
        self.p15=0
        self.lb3["text"]=" "
        self.lb2["text"]=f"{'Player 1':<}" + f"{self.p15:>5}" + f'{"x":^16}'+ f"{self.cpu5:<4}" + f"{'Computador':<6}"
        self.lb6["text"]=f"{' P1':>}"+f"{'x':^3}"+f"{'CPU':<}" 

    def reset2(self,event):
        self.cpu5=0
        self.p15=0
        self.lb2["text"]=f"{'Player 1':<}" + f"{self.p15:>5}" + f'{"x":^16}'+ f"{self.cpu5:<4}" + f"{'Computador':<6}"
        self.lb6["text"]=f"{' P1':>}"+f"{'x':^3}"+f"{'CPU':<}" 

    def jogar(self):
        t1=self.num.get().isnumeric()
        self.lb5["text"]=" "
        if self.escolha.get()=="par" or self.escolha.get()=="impar":
            self.lb5["text"]=" "
            if t1==True:
                self.lb5["text"]=" "
                if int(self.num.get())<10 and int(self.num.get())>=0:
                    cpu1=randint(0,10) 
                    p1=int(self.num.get())
                    t=par_impar(cpu1,p1,self.escolha.get())
                    self.lb3["text"]=t[0]
                    self.lb6["text"]=f"{p1:>}"+f"{'x':^3}"+f"{cpu1:<}"

                    if t[1]=="p":
                        self.p15+=1 
                    else:
                        self.cpu5+=1
                        
                    self.lb2["text"]=f"{'Player 1':<}" + f"{self.p15:>5}" + f'{"x":^16}'+ f"{self.cpu5:<4}" + f"{'Computador':<6}"
                else:
                    self.lb5["text"]="Erro digite um numero entre 0 e 10"
            else:
                self.lb5["text"]="Digite apenas numeros de 0 ate 10"
        else:
            self.lb5["text"]="Erro escolha ou par ou impar."

    def jogar2(self,event):
        t1=self.num.get().isnumeric()
        self.lb5["text"]=" "
        if self.escolha.get()=="par" or self.escolha.get()=="impar":
            self.lb5["text"]=" "
            if t1==True:
                self.lb5["text"]=" "
                if int(self.num.get())<10 and int(self.num.get())>=0:
                    cpu1=randint(0,10) 
                    p1=int(self.num.get())
                    t=par_impar(cpu1,p1,self.escolha.get())
                    self.lb3["text"]=t[0]
                    self.lb6["text"]=f"{p1:>}"+f"{'x':^3}"+f"{cpu1:<}"

                    if t[1]=="p":
                        self.p15+=1 
                    else:
                        self.cpu5+=1
                        
                    self.lb2["text"]=f"{'Player 1':<}" + f"{self.p15:>5}" + f'{"x":^16}'+ f"{self.cpu5:<4}" + f"{'Computador':<6}"
                else:
                    self.lb5["text"]="Erro digite um numero entre 0 e 10"
            else:
                self.lb5["text"]="Digite apenas numeros de 0 ate 10"
        else:
            self.lb5["text"]="Erro escolha ou par ou impar." 


c=0
raiz=Tk()
janela=Janela(raiz)
raiz.geometry("900x850+550+100")
raiz.title("Jogo de para ou impar")
raiz["bg"]=cinza1
raiz.mainloop()
