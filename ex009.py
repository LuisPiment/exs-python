"""Objetivos:
Principal: abrir uma janela de login e com mutiplas funcoes com o tkinter
secundarios:
Funçoes:
criação de conta(Exegira: nome de utilizador,senha 2 vezes mas iguais, email(sem verificação mesmo),função de multiplaescolha de continente) )
Login
se o login for um sucesso tera as proximas funçoes:
mudança de senha exegindo o email
mudança de email exegindo a senha
mudana de de nome de utilizador sem exegir nada
  """
from tkinter import *
from Cores import *
class Pograma:
    def __init__(self,raiz1):
        self.fr1=Frame(raiz1,bg=cinza_escuro)
        self.fr1.pack()
        
        self.lb1=Label(self.fr1,bg=verde_esmeralda,text="Ola")
        self.lb1.pack()
        
    
        self.bt1=Button(self.fr1,bg=cinza_claro,text="ok")
        self.bt1.pack()



raiz=Tk()
janela=Pograma(raiz)
raiz.geometry("400x400+800+300")
raiz["bg"]=cinza_escuro


raiz.mainloop()
