"""Objetivos:
Principal: abrir uma janela de login e com mutiplas funcoes com o tkinter
secundarios:
Funçoes:
criação de conta(Exegira: nome de utilizador,senha, email(sem verificação mesmo),função de multiplaescolha de continente) ~
regras:
    senha tem de conter letras e numeros, tem de ter mais de 8 digitos e tem de ser igual nas duas verificaçoes,
    nome de utilizador nao pode ser igual a nenhum do seu banco de dados ou lista,
    email pelo menos tem de ter o @)
Login(nome de usario e senha)
se o login for um sucesso tera as proximas funçoes:
mudança de senha exegindo o email
mudança de email exegindo a senha
mudana de de nome de utilizador sem exegir nada
  """
from tkinter import *
from Cores_e_fontes import *
class Pograma:
    def __init__(self,raiz1):
        self.fr1=Frame(raiz1,bg=cinza_escuro)
        self.fr1.pack()
        self.fr2=Frame(raiz,bg=cinza_escuro)
        self.fr2.pack()

        self.fr3=Frame(raiz,bg=cinza_escuro)
        self.fr3.pack()

        self.fr4=Frame(raiz,bg=cinza_escuro)
        self.fr4.pack()

        self.fr5=Frame(raiz,bg=cinza_escuro)
        self.fr5.pack()

        self.fr6=Frame(raiz,bg=cinza_escuro)
        self.fr6.pack()
        
        self.loca1=Label(self.fr1,bg=cinza_escuro,text="",)
        self.loca1.pack()

        self.lb1=Label(self.fr1,bg=cinza_escuro,text="Projeto de Login",font=f_titulo,fg="white",)
        self.lb1.pack()
        
        self.loca2=Label(self.fr1,bg=cinza_escuro,text="",pady=30)
        self.loca2.pack()

        self.bt1=Button(self.fr2,bg=cinza_claro,text="Login",font=f_butao,fg=verde_esmeralda)
        self.bt1.pack()
        self.bt1["relief"]="ridge"
        self.bt1["border"]=5

        self.loca3=Label(self.fr2,bg=cinza_escuro,text="",pady=2)
        self.loca3.pack()

        self.bt2=Button(self.fr2,bg=cinza_claro,text="Criar Conta",font=f_butao,fg=azul_marinho,command=self.criar_conta)
        self.bt2.pack()
        self.bt2["relief"]="ridge"
        self.bt2["border"]=5

    def criar_conta(self):
        self.lb1.pack_forget()
        self.loca1.pack_forget()
        self.loca2.pack_forget()
        self.loca3.pack_forget()
        self.bt1.pack_forget()
        self.bt2.pack_forget()
        self.nu1=Label(self.fr1,text="Nome de Utilizador:",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.nu1.pack(side=LEFT,pady=20)
        self.nu2=Entry(self.fr1,width=20,font=f_butao,bg=cinza_claro,fg="white")
        self.nu2.pack(side=LEFT,pady=20)

        self.loca4=Label(self.fr1,bg=cinza_escuro,text="                                    ",pady=30)
        self.loca4.pack(side=LEFT)

        self.se1=Label(self.fr2,text="Senha:",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.se1.pack(side=LEFT,pady=20)
        self.se2=Entry(self.fr2,font=f_butao,bg=cinza_claro,fg="white",width=20)
        self.se2.pack(side=LEFT,pady=20)

        self.se3=Label(self.fr3,text="Senha:",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.se3.pack(side=LEFT,pady=8)
        self.se3=Label(self.fr4,text="(obs:As duas tem de ser igual):",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.se3.pack()
        self.se4=Entry(self.fr3,font=f_butao,bg=cinza_claro,fg="white")
        self.se4.pack(side=LEFT,pady=8)
        
        self.em1=Label(self.fr4,text="Email:",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.em1.pack(side=LEFT,pady=8)
        
        self.em2=Entry(self.fr4,font=f_butao,bg=cinza_claro,fg="white",width=30)
        self.em2.pack(side=LEFT,pady=8)


        self.em1=Label(self.fr5,text=f"{'Continente residente:':<70}",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.em1.pack()
        self.escolha=StringVar

        self.eur=Radiobutton(self.fr5,text=f"{'Europa':<40}",font=f_butao,value="europa",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.eur.pack()
        self.amn=Radiobutton(self.fr5,text=f"{'America do Norte':<34}",font=f_butao,value="amn",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.amn.pack()
        self.ams=Radiobutton(self.fr5,text=f"{'America do Sul':<36}",font=f_butao,value="ams",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.ams.pack()
        self.asia=Radiobutton(self.fr5,text=f"{'Asia':<43}",font=f_butao,value="asia",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.asia.pack()
        self.anta=Radiobutton(self.fr5,text=f"{' Antartida    ':<40}",font=f_butao,value="anta",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.anta.pack()
        self.oc=Radiobutton(self.fr5,text=f"{'Oceania':<40}",font=f_butao,value="oc",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.oc.pack()

raiz=Tk()
janela=Pograma(raiz)
raiz.geometry("600x600+700+200")
raiz["bg"]=cinza_escuro


raiz.mainloop()
