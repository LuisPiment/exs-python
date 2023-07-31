from Ferramentas import *
"""ex=
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

    Possua uma classe chamada Ponto, com os atributos x e y.
    Possua uma classe chamada Retangulo, com os atributos largura e altura(2d).
    Possua uma função para imprimir os valores da classe Ponto
    Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
    Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
    A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
    O valor do centro do objeto deve ser mostrado na tela
    Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo."""

class Ponto():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def info2(self):
        cabeçalhototal(f"As cordenadas do ponto são: x={self.x} e y={self.y}")
class Rentagulo(Ponto):
    def __init__(self,altura,largura,x,y):
        self.largura=largura
        self.altura=altura
        super().__init__(x,y)
        self.centrox=self.x + (self.largura/2)
        self.centroy=self.y + (self.altura/2)
    def info1(self):
        cabeçalhototal(f"A altura do rentagulo é {self.altura} e sua largura é de {self.largura}")
    def centro(self):
        cabeçalhototal(f"O centro do rentagulo é nas cordenadas x={self.centrox} e y={self.centroy}")
    def mudar(self):
        while True:
            c=str(input("Deseja mudar o valor do x e do y?(S/N):")).strip().lower()[0]
            if c in "s":
                x1=str(input("Digite o novo valor de x: "))
                y1=str(input("Digite o novo valor de y: "))
                x2=x1.isnumeric()
                y2=y1.isnumeric()
                if x2==True and y2==True:
                    print("Mudança feita")
                    self.x1=int(self.x)
                    self.y1=int(self.y)
                    break
                else:
                    print("Erro por favor digite novamente os valores")
            elif c=="n":
                break
            else:
                print("por favor digite apenas sim ou nao")

                
            
                    

p1=Rentagulo(10,18,3,4)
p1.info2()
p1.info1()
p1.centro()
p1.mudar()
