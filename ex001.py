from Ferramentas import cabeçalho
class Restaurante():
    """Simulação de um restaurante"""
    def __init__(self,res_nome,tipo_cozinha):
        self.res_nome=res_nome
        self.tipo_cozinha=tipo_cozinha
    def restaurante_descrição(self):
        cabeçalho(f"{'O nome do restaurante é'}  {self.res_nome.title()}"
                 f" {'O tipo de cozinha é'}  {self.tipo_cozinha.title()}")
    def restaurante_aberto(self):
        cabeçalho(self.res_nome.title() + " esta aberto")


res1=Restaurante("Obra del darte","italiana")
res2=Restaurante("Obra divina","portuguesa")
res3=Restaurante("Central","brasileira")
res1.restaurante_descrição()
res2.restaurante_descrição()
res3.restaurante_descrição()








