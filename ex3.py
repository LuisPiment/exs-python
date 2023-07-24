from Ferramentas import cabeçalho
class Casa():
    def __init__(self,quant_quartos):
        self.quant_quartos=quant_quartos
        self.metrosquadrados=metrosquadrados()
    def situação(self):
        cabeçalho(f"A casa tem {self.quant_quartos} quartos e a area da casa é {self.metrosquadrados.area_1_quarto*self.quant_quartos}")

class metrosquadrados():
    def __init__(self,largura=0,comprimento=0):
        self.largura=largura
        self.comprimento=comprimento
        self.area_1_quarto=largura*comprimento
    def lar_com(self,lar=0,com=0):
        self.lar=self.largura
        self.com=self.comprimento
        self.area_1_quarto=(com*lar)

casa1=Casa(5)
casa1.metrosquadrados.lar_com(3,5)
casa1.situação()


    
