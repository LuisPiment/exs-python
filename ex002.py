from Ferramentas import cabeçalho
import datetime
at=datetime.date.today().year
class Usuario():
    """Simulação de um cadastro de usario"""
    def __init__(self,p_nome,u_nome,data_de_nascimento,email):
        self.p_nome=p_nome
        self.u_nome=u_nome
        self.data_de_nacimento=data_de_nascimento
        self.email=email
    def des_usuario(self):
        cabeçalho(f"{'O seu primeiro nome é '}{self.p_nome.title()}\n{'  O seu ultimo nome é '}{self.u_nome.title()}"
                  f"\n{'  A sua idade é '}{at-self.data_de_nacimento} \n{'  O seu email é '}{self.email}")
    def saudação(self):
        cabeçalho(f"{'Ola usario '}{self.p_nome.title()}{',tenha um bom dia'}")
n=[]
for c in range (0,4):
    n.append(str(input("Digite o sue primeiro nome ")))
    n.append(str(input("Digite o sue ultimo nome ")))
    n.append(int(input("Digite a sua data de nacimento ")))
    n.append(str(input("Digite o seu email ")))
    n[0]=Usuario(n[0],n[1],n[2],n[3])
    n[0].des_usuario()
    n[0].saudação()
    n.clear()

    
