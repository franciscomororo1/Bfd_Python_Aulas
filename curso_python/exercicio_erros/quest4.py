try:
   arquivo = open (dados.txt)
except NameError:
    print("Arquivo não existe")
finally:
    print("Arquivo Fechado")