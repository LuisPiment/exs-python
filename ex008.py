with open("teste.txt") as file:
    contents = file.read()
    contents = contents.replace("Portugal", "")
with open("teste.txt", "w") as file:
    file.write(contents)







