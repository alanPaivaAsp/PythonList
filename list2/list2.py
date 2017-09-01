'''EXERCISE 1
Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, 
caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''
val_a = False
val_b = False
val_c = False
print('Digite os 3 lados de um triangulo(A,B e C) em CM: ')
a = int(input('A : '))
b = int(input('B : '))
c = int(input('C : '))

if a > ((b-c)*-1) and a < (b+c):
  val_a = True
if b > ((a-c)*-1) and b < (a+c):
  val_b = True
if c > ((a-b)*-1) and c < (a+b):
  val_c = True
if val_a == True and val_b == True and val_c == True:
  print('Valores validos para se formar um triangulo')
if a == b and a == c and b == c:
  print('E tambem o triangulo e um equilatero')
elif a != b and a !=c and b!= c:
  print('E tambem e um triangulo escaleno')
else:
  print ('E tambem um triangulo isosceles \n\n\n\n\n\n\n\n\n')
   
   
  

 
  
#__________________________________________________________________________________________________________

'''
EXERCISE 2
Determine se um ano é bissexto. Verifique no Google como fazer isso...'''
#__________________________________________________________________________________________________________
'''
EXERCISE 3
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. 
Caso contrário mostrar tais variáveis com o conteúdo ZERO.'''
#__________________________________________________________________________________________________________
'''
EXERCISE 4
Faça um Programa que leia três números e mostre o maior deles.'''
#__________________________________________________________________________________________________________
'''
EXERCISE 5
Faça um Programa que leia três números e mostre o maior e o menor deles.'''
#__________________________________________________________________________________________________________
''' 
EXERCISE 6
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. 
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$'''
#__________________________________________________________________________________________________________

''' 
EXERCISE 7
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
Obs. : somente são vendidos um número inteiro de latas.'''