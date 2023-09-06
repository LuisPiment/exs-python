from pydantic import BaseModel
from typing import Optional,List
from random import randint
import sqlite3




class Produto(BaseModel):
    id: Optional [int]=randint(100,999) 
    nome_Prod: str
    vendedor:List[Usuario]
    detalhes: str
    preço:float
    disponivel: bool =False


class Pedido(BaseModel):
    id: Optional [int]=randint(100,999) 
    produto:Produto
    comprador:Usuario
    quantidade: int
    status_entrega:bool=False
    destinho: str

class Usuario(BaseModel):
    id: Optional [int]=randint(100,999) 
    nome: str 
    idade: int
    email: str
    pedidos: List[Pedido]
    produtos_a_venda: List[Produto]
    minhas_vendas: List[Pedido]
    telefone: str

