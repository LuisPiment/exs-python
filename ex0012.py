import sqlite3

Conexao= sqlite3.connect("Dados")
Cursor=Conexao.cursor()
#Cursor.execute("CREATE TABLE Minha_Tabela(Nome text,Idade real,Cor text)")
#Conexao.commit()
Cursor.execute("INSERT INTO Minha_Tabela Values('rosa',17,'red')")
Cursor.execute("INSERT INTO Minha_Tabela Values('rodrigo',14,'Roxo')")
Cursor.execute("INSERT INTO Minha_Tabela Values(null,12,'azul')")
Cursor.execute("INSERT INTO Minha_Tabela Values('carolina',null,null)")
Cursor.execute("INSERT INTO Minha_Tabela Values(null,null,'roxo')")

#consulta=Cursor.execute("SELECT * FROM Minha_Tabela  ").fetchall()
#for c in consulta:
 #   print(c)

"""
consulta=Cursor.execute("Select * FROM Minha_Tabela WHERE Nome='rosa'").fetchall()
print(consulta)
consulta1=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Idade>13").fetchall()
print(consulta1)
consulta2=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Idade<=14").fetchall()
print(consulta2)
consulta3=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Nome<>'Rodrigo'").fetchall()
print(consulta3)
consulta4=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Idade BETWEEN 12 AND 16").fetchall()
print(consulta4)
print(" ")
consulta5=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Nome LIKE 'r%'").fetchall()
print(consulta5)
consulta6=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Nome LIKE '%a'").fetchall()
print(consulta6)
consulta7=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Nome LIKE '%ro%'").fetchall()
print(consulta7)
consulta8=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Nome LIKE '_o%'").fetchall()
print(consulta8)
consulta9=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Nome LIKE 'r____%'").fetchall()
print(consulta9)
consulta10=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Nome LIKE 'r%o'").fetchall()
print(consulta10)
"""
"""
consulta=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Nome IN ('rosa','rodrigo')").fetchall()
print(consulta)


consulta1=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Idade<16 AND NOT Cor='Roxo' ").fetchall()
print(consulta1)


consulta2=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Nome ='rodrigo' or Nome='rosa'").fetchall()
print(consulta2)
"""
"""
consulta=Cursor.execute("SELECT * FROM Minha_Tabela Order by Idade").fetchall()
print(consulta)

consulta1=Cursor.execute("SELECT * FROM Minha_Tabela Order by Idade,Nome").fetchall()
print(consulta1)

consulta2=Cursor.execute("SELECT * FROM Minha_Tabela Order by Idade DESC").fetchall()
print(consulta2)
"""
"""
consulta=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Nome is NULL").fetchall()
print(consulta)
consulta1=Cursor.execute("SELECT * FROM Minha_Tabela WHERE Idade is not NULL").fetchall()
print(consulta1)"""

consulta1=Cursor.execute("UPDATE Minha_Tabela SET Nome='Francisco ' WHERE Cor= 'azul' ").fetchall()
consulta3=Cursor.execute("UPDATE Minha_Tabela SET Idade=19 WHERE Idade is NULL ").fetchall()
consulta2=Cursor.execute("UPDATE Minha_Tabela SET Nome='Dulce' WHERE Nome is Null ").fetchall()
consulta4=Cursor.execute("UPDATE Minha_Tabela SET Cor='verde' WHERE Cor is Null ").fetchall()

consulta5=Cursor.execute("DELETE FROM Minha_Tabela where nome is 'rosa'").fetchall()


"""consulta=Cursor.execute("SELECT * FROM Minha_Tabela LIMIT 3 ").fetchall()
for c in consulta:
   print(c)"""
consulta=Cursor.execute("SELECT count(Idade) FROM Minha_Tabela LIMIT 3 ").fetchall()
print(consulta)