from Ferramentas import *
"""
ex:Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer,Perfil(Para ver as estatisticas atuais da pessoa). Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
Fonte:https://wiki.python.org.br/ExerciciosClasses
"""

class Pessoa():
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        self.idat=self.idade
    
    def perfil(self):
        cabeçalhototal(f"Nome={self.nome}\n  Idade={self.idade}\n  Peso={self.peso}\n  Altura={self.altura}")
    
    def envelhecer(self,id):
        self.idat+=id
        cabeçalhoinicio(f"Voce envelheceu {id} anos e tem {self.idat} anos ")
        if self.idade<21 and self.idat<21:
            self.altura+=(id*0.5)
            cabeçalhofinal(f"A sua altura aumentou para {self.altura} cm")
        elif self.idade<21 and self.idat>21:
            self.altura+=(21-self.idade)*0.5
            cabeçalhofinal(f"A sua altura aumentou para {self.altura}")
        self.idade=self.idat
    
    def engordar(self,pe):
        self.peso+=pe
        cabeçalhototal(f"Voce engordou {pe} kg e tem {self.peso} kg")
    
    def emagrecer(self,pe):
        self.peso-=pe
        cabeçalhototal(f"Voce emagreceu {pe} kg e tem {self.peso} kg")    
    
    def crescer(self,cm):
        self.altura+=cm
        cabeçalhototal(f"Voce cresceu {cm} cm e tem {self.altura} cm")

    
p1=Pessoa("Luis",15,90,170)
while True:
    test=(int(input("Digite a função que quer(temos:1=perfil,2=envelhecer,3=emagrecer,4=crescer,5=engordar,6=Para parar): ")))
    if test==1:
        p1.perfil()
    elif test==2:
        n1=int(input("Quantos anos quer envelhecer: "))
        p1.envelhecer(n1)
    elif test==3:
        n2=int(input("Digite quanto kg quer emagrecer: "))
        p1.emagrecer(n2)
    elif test==4:
        n3=int(input("Digite quantos cm quer crescer: "))
        p1.crescer(n3)
    elif test==5:
        n4=int(input("Digite quantos kg quer engordar: "))
        p1.engordar(n4)
    elif test==6:
        break
    else:
        cabeçalhototal("Opção indesponivel escolha dentro as 5 opções(1,2,3,4,5)")
cabeçalhototal("Espero que tenha gostado")



    





    

    
