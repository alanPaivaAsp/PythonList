# EXERCICIO DE ESTRUTURA ANINHADA
minutos = int(input("Minutos utilizados: "))
if minutos < 200:
    preço = 0.20
else:
    if minutos <= 400:
        preço = 0.18
    else:
        preço = 0.15

print("Conta telefônica: R$%6.2f" % (minutos * preço,"\n \n \n \n \n \n"))

#_________________________________________________________________________________

'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
'''
km = float(input("Quantidade de KM percorridos: "))
dias = int(input("Quantidade de dias alugados: "))
print("Total R$: %.2f \n \n \n \n \n", %(dias*60)+(km*0.15))

#_________________________________________________________________________________

'''Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
Considere que um fumante perde 10 minutos de vida a cada cigarro, 
calcule quantos dias de vida um fumante perderá. Exiba o total de dias.'''

