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

        self.bt1=Button(self.fr2,bg=cinza_claro,text="Login",font=f_butao,fg=verde_esmeralda,command=self.login)
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
        self.se5=Label(self.fr4,text="(obs:As duas tem de ser igual):",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.se5.pack()
        self.se4=Entry(self.fr3,font=f_butao,bg=cinza_claro,fg="white")
        self.se4.pack(side=LEFT,pady=8)
        
        self.em1=Label(self.fr4,text="Email:",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.em1.pack(side=LEFT,pady=8)
        
        self.em2=Entry(self.fr4,font=f_butao,bg=cinza_claro,fg="white",width=30)
        self.em2.pack(side=LEFT,pady=8)


        self.con=Label(self.fr5,text=f"{'Continente residente:':<70}",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.con.pack()
        self.escolha=StringVar()

        self.eur=Radiobutton(self.fr5,text=f"{'Europa':<40}",font=f_butao,value="Europa",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.eur.pack()
        self.amn=Radiobutton(self.fr5,text=f"{'America do Norte':<34}",font=f_butao,value="America do Norte",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.amn.pack()
        self.ams=Radiobutton(self.fr5,text=f"{'America do Sul':<36}",font=f_butao,value="America do Sul",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.ams.pack()
        self.asia=Radiobutton(self.fr5,text=f"{'Asia':<43}",font=f_butao,value="Asia",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.asia.pack()
        self.anta=Radiobutton(self.fr5,text=f"{' Antartida    ':<40}",font=f_butao,value="Antartida",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.anta.pack()
        self.oc=Radiobutton(self.fr5,text=f"{'Oceania':<40}",font=f_butao,value="Oceânia",variable=self.escolha,bg=cinza_escuro,fg=cinza_claro)
        self.oc.pack()

        self.erro=Label(self.fr6,text="",bg=cinza_escuro,fg="red",font=f_butao)
        self.erro.pack()

        self.cc=Button(self.fr6,bg=cinza_claro,text="Criar Conta",font=f_butao,fg=azul_marinho,command=self.criar)
        self.cc.pack()
    def criar(self):
       
       self.nome=self.nu2.get()
       self.senha1=self.se2.get()
       self.senha2=self.se4.get()
       self.email=self.em2.get()
       self.continente=self.escolha.get()
       if len(self.nome)>2 and self.nome not in ("ex009_Logins.py"):
           if self.senha1==self.senha2:
               if len(self.senha1)>=8:
                    if self.senha1.isnumeric()==False and self.senha1.isalpha()==False:
                        if "@" in self.email and len(self.email)>2:
                            if self.continente=="Europa" or self.continente=="America do Norte" or self.continente=="America do Sul" or self.continente=="Asia" or self.continente=="Antartida" or self.continente=="Oceânia":
                                self.arq=open("ex009_Logins.py","a")
                                self.arq.write(f"\n{self.nome}")
                                self.arq.write(f"\n{self.continente}")
                                self.arq.write(f"\n{self.senha1}")
                                self.arq.write(f"\n{self.email}")
                                self.arq.close()
                                self.loca4.pack_forget()
                                self.nu1.pack_forget()
                                self.nu2.pack_forget()
                                self.se1.pack_forget()
                                self.se2.pack_forget()
                                self.se3.pack_forget()
                                self.se4.pack_forget()
                                self.se5.pack_forget()
                                self.em1.pack_forget()
                                self.em2.pack_forget()
                                self.con.pack_forget()
                                self.eur.pack_forget()
                                self.amn.pack_forget()
                                self.ams.pack_forget()
                                self.asia.pack_forget()
                                self.anta.pack_forget()
                                self.oc.pack_forget()
                                self.nu1.pack_forget()
                                self.erro.pack_forget()
                                self.cc.pack_forget()
                                self.loca1=Label(self.fr1,bg=cinza_escuro,text="",)
                                self.loca1.pack()

                                self.lb1=Label(self.fr1,bg=cinza_escuro,text="Projeto de Login",font=f_titulo,fg="white",)
                                self.lb1.pack()
        
                                self.loca2=Label(self.fr1,bg=cinza_escuro,text="",pady=30)
                                self.loca2.pack()

                                self.bt1=Button(self.fr2,bg=cinza_claro,text="Login",font=f_butao,fg=verde_esmeralda,command=self.login)
                                self.bt1.pack()
                                self.bt1["relief"]="ridge"
                                self.bt1["border"]=5

                                self.loca3=Label(self.fr2,bg=cinza_escuro,text="",pady=2)
                                self.loca3.pack()

                                self.bt2=Button(self.fr2,bg=cinza_claro,text="Criar Conta",font=f_butao,fg=azul_marinho,command=self.criar_conta)
                                self.bt2.pack()
                                self.bt2["relief"]="ridge"
                                self.bt2["border"]=5

                                self.erro["text"]=" "
                            else:
                                self.erro["text"]="Por favor escolha um dos continentes"
                        else:
                            self.erro["text"]="Por favor digite um email existente"
                    else:
                        self.erro["text"]="A sua senha tem de conter letras e numeros"
               else:
                   self.erro["text"]="A sua senha tem de ter mais de 8 letras"
           else:
               self.erro["text"]="As senhas tenhem de ser iguais,por favor tente novamente"
       else:
           self.erro["text"]="Esse nome ja foi registrado, tente outro"
    def login(self):
        self.lb1.pack_forget()
        self.loca1.pack_forget()
        self.loca2.pack_forget()
        self.loca3.pack_forget()
        self.bt1.pack_forget()
        self.bt2.pack_forget()
        self.loca6=Label(self.fr1,bg=cinza_escuro,text=" Introduza os seus dados:",font=f_titulo,pady=30,fg=verde_esmeralda)
        self.loca6.pack(side=LEFT,pady=20)
        self.nu1=Label(self.fr2,text="Utilizador:",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.nu1.pack(side=LEFT,pady=15)
        self.nu2=Entry(self.fr2,width=20,font=f_butao,bg=cinza_claro,fg="white")
        self.nu2.pack(side=LEFT,pady=15)
        self.loca5=Label(self.fr2,bg=cinza_escuro,text="                                             ",)
        self.loca5.pack(side=LEFT)

        self.se1=Label(self.fr3,text="Senha:",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.se1.pack(side=LEFT,pady=15)
        self.se2=Entry(self.fr3,font=f_butao,bg=cinza_claro,fg="white",width=20)
        self.se2.pack(side=LEFT,pady=15)
        self.loca4=Label(self.fr3,bg=cinza_escuro,text="                                    ")
        self.loca4.pack(side=LEFT)
        
        self.em1=Label(self.fr4,text="Email:",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.em1.pack(side=LEFT,pady=15)
        
        self.em2=Entry(self.fr4,font=f_butao,bg=cinza_claro,fg="white",width=30)
        self.em2.pack(side=LEFT,pady=15)

        self.erro=Label(self.fr6,text="",bg=cinza_escuro,fg="red",font=f_butao)
        self.erro.pack(pady=15)

        self.cc=Button(self.fr6,bg=cinza_claro,text="Logar",font=f_butao,fg=azul_marinho,command=self.logar)
        self.cc.pack()
    def logar(self):
        self.contador=0

        self.nome=self.nu2.get()
        self.senha=self.se2.get()
        self.email=self.em2.get()
        self.lista= [line.rstrip() for line in open('ex009_Logins.py')]
        
        
        if self.nome in self.lista:
            self.contador+=1
        
        if self.contador==1:
            for self.pos,self.c1 in enumerate(self.lista):
                if self.nome==self.c1:
                    if self.lista[(self.pos+2)]==self.senha:
                        if self.lista[(self.pos+3)]==self.email:
                            self.nu2.pack_forget()
                            self.se2.pack_forget()
                            self.nu1.pack_forget()
                            self.se1.pack_forget()
                            self.em1.pack_forget()
                            self.em2.pack_forget()
                            self.erro.pack_forget()
                            self.loca4.pack_forget()
                            self.loca5.pack_forget()
                            self.cc.pack_forget()

                            if self.nome=="luis9021":
                                self.loca6["text"]="Funções de ADM"

                                self.bt2=Button(self.fr2,bg=cinza_claro,text="Mudança de senha",font=f_butao,fg=azul_marinho,command=self.musenha(self.senha))
                                self.bt2.pack()
                                self.bt2["relief"]="ridge"
                                self.bt2["border"]=5

                                self.loca4=Label(self.fr3,bg=cinza_escuro,text="                                    ",pady=15)
                                self.loca4.pack(side=LEFT)

                                self.bt2=Button(self.fr4,bg=cinza_claro,text="Mudanca de email",font=f_butao,fg=azul_marinho)
                                self.bt2.pack()
                                self.bt2["relief"]="ridge"
                                self.bt2["border"]=5

                                self.loca4=Label(self.fr3,bg=cinza_escuro,text="                                    ",pady=15)
                                self.loca4.pack(side=LEFT)

                                self.bt2=Button(self.fr4,bg=cinza_claro,text="Apagar conta",font=f_butao,fg=azul_marinho)
                                self.bt2.pack()
                                self.bt2["relief"]="ridge"
                                self.bt2["border"]=5

                            else:
                                self.loca6["text"]="Funções de usuario"
                                self.bt2=Button(self.fr2,bg=cinza_claro,text="Mudança de senha",font=f_butao,fg=azul_marinho,padx=15,pady=15,command=self.musenha(self.senha))
                                self.bt2.pack()
                                self.bt2["relief"]="ridge"
                                self.bt2["border"]=5

                                self.loca4=Label(self.fr3,bg=cinza_escuro,text="                                    ",pady=15)
                                self.loca4.pack(side=LEFT)

                                self.bt2=Button(self.fr2,bg=cinza_claro,text="Mudanca de email",font=f_butao,fg=azul_marinho,padx=15,pady=15)
                                self.bt2.pack()
                                self.bt2["relief"]="ridge"
                                self.bt2["border"]=5
                        else:
                            self.erro["text"]="Email errado tente novamente"
                    else:
                        self.erro["text"]="Senha incorreta, tente novamente"
                

        else:
            self.erro["text"]="Por favor insira um nome valido"





                            
    def musenha(self,senha):
        self.se1=Label(self.fr2,text="Senha:",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.se1.pack(side=LEFT,pady=20)
        self.se2=Entry(self.fr2,font=f_butao,bg=cinza_claro,fg="white",width=20)
        self.se2.pack(side=LEFT,pady=20)

        self.se3=Label(self.fr3,text="Senha:",font=f_butao,bg=cinza_escuro,fg=cinza_claro)
        self.se3.pack(side=LEFT,pady=8)
        self.se4=Entry(self.fr3,font=f_butao,bg=cinza_claro,fg="white")
        self.se4.pack(side=LEFT,pady=8)

        self.bt2=Button(self.fr2,bg=cinza_claro,text="Mudar",font=f_butao,fg=azul_marinho,padx=15,pady=15,command=self.mudar(senha,self.se2))
        self.bt2.pack()
        self.bt2["relief"]="ridge"
        self.bt2["border"]=5

        self.erro=Label(self.fr3,text="",font=f_butao,bg=cinza_escuro,fg="red")
        self.erro.pack()

    def mudar(self,senha_ant,senhaatt):
        if self.se2==self.se4:
            for pos,c in enumerate(self.lista):
                if c==senha_ant:
                    self.lista[pos]=senhaatt
        else:
            self.erro["text"]="As senha tenhem de ser iguais"

                                



                        
                    

                
        







        

           
            





raiz=Tk()
janela=Pograma(raiz)
raiz.geometry("600x600+700+200")
raiz["bg"]=cinza_escuro


raiz.mainloop()
