numero = int( input("Digite um número (ou 0 para sair):") )
while numero != 0:
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
    numero = int( input("Digite um número (ou 0 para sair):") )
print("Fim do programa")