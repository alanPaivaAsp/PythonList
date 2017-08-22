#--------------------------------------------------------------------------------------------

''' #Exercise 1 : 
Faça um programa que peça dois números inteiros e imprima a soma desses dois números '''
numeros = list()
soma = 0
#Recebendo os valores e adicionando no array numeros[]
for x in range (0,2):
   print("Digite o ",x+1,"numero:")
   numeros.append(int(input()))
   #somando o valor recebido no array numeros[]
   soma += numeros[x]
#printando o valor da soma depois de ter perguntado os 2 valores no FOR acima
print("SOMA:",soma,"\n \n \n \n \n")
#--------------------------------------------------------------------------------------------

''' #Exercise 2 : 
Escreva um programa que leia um valor em metros e o exiba convertido em milímetros '''
#Recebendo o valor em metros
metros = int(input("Digite o valor em metros: "))
#Imprimindo em Milimetros(metros * 1000)
print(metros*1000,"MM\n \n \n \n \n")


#--------------------------------------------------------------------------------------------

''' #Exercise 3 : 
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
o total em segundos. '''

#Recebendo os valores de Dias, horas, minutos e segundos
dias = int(input("Digite quantidade de dias: "))
dias *= 86400
horas = int(input("Digite quantidade em horas:"))
horas *= 3600
minutos = int(input("Digite quantidade em minutos:"))
minutos *=60
segundos = int(input("Digite quantidade em segundos:"))
#somando o total em segundos
segundos +=dias+horas+minutos
#Imprimindo o valor
print("Total em segundos:",segundos,"\n \n \n \n \n")

#--------------------------------------------------------------------------------------------

''' #Exercise 4 : 
Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário. '''
#Recebendo os valores
sal_atual = float(input("Digite seu salário atual: "))
por_aumento = float(input("Digite porcentagem de aumento:"))
#Calculando o aumento e o novo salário
aumento = (sal_atual*aumento)/100
novo_sal = aumento + sal_atual
#printando na tela os resultados
print("O valor do aumento será: ",aumento)
print("O novo salário será: ",novo_sal, "\n \n \n \n \n")


#--------------------------------------------------------------------------------------------

''' #Exercise 5 : 
Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar. '''
#Recebendo os valores
preco = float(input("Digite o valor da mercadoria: "))
percent_desc = float(input("Digite o percentual de desconto: "))
#Calculando os descontos
desconto = (preco*percent_desc)/100
novo_valor = desconto + preco
# Imprimindo o resultado
print("Valor do desconto: ",desconto,"R$")
print("Novo valor: ",novo_valor,"R$ \n \n \n \n \n")

#--------------------------------------------------------------------------------------------

''' #Exercise 6 : 
Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
esperada para a viagem.  '''
#Recebendo DeltaS e VM
dist = float(input("Digite a distância da viagem em KM: "))
vm = float(input("Digite a velocidade média esperada KM/H: "))
#calculando com a formula de Velocidade média
dt = vm/dist
#imprimindo o resultado
print("O tempo estimado de viagem é: ",dt,"horas \n \n \n \n \n")

#--------------------------------------------------------------------------------------------

''' #Exercise 7 : 
Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32'''
celsius = float(input("Digite a temperatura em Celsius"))
fahren = ((9*celsius)/5)+32
print("F°: ",fahren,"\n \n \n \n \n")

#--------------------------------------------------------------------------------------------

''' #Exercise 8 : 
Faça agora o contrário, de Fahrenheit para Celsius. '''

#--------------------------------------------------------------------------------------------

''' #Exercise 9 : 
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.'''

#--------------------------------------------------------------------------------------------

''' #Exercise 10 : 
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.'''

#--------------------------------------------------------------------------------------------

''' #Exercise 11 : 
Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
a um milhão. '''

#--------------------------------------------------------------------------------------------

