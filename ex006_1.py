"""Preparações para o projeto do ex006"""
cinza1="#1C1C1C"
cinza2="#A9A9A9"
branco="#ffffff"
preto="_#000000"
azul_claro="#E0FFFF"
azul2="#A0E0D0"
vermelho="red"
fonte1=("Time New Roman",40,"bold")
fonte2=("Verdana",27,"bold")
fonte3=("Verdana",15,"bold")
fonte4=("Verdana",100,"bold")
def par_impar(cpu,p1,pi2):
    u=" "

    s=p1+cpu
    if s%2==1:
        pi=("impar")
    else:
        pi=("par")
    if pi[0]==pi2[0]:
        t=f"O player 1 Ganhou pois a soma deu {s}"
        u="p"
    else:
        t=f"O player 1 perdeu pois a soma deu {s}"
        u="c"
    return t,u
    


