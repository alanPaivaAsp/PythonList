'''
Exersise 1

Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido
'''
while True:
	nota = float(input('Digite uma nota de  0 à 10: '))
	if nota >= 0 and nota <= 10:
		break
	
#_______________________________________________________
	
'''
Exersise 2

Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
	nome = str(input('Login: '))
	password = str(input('Senha: '))
	if not nome == password:
		break
	else:
		print("Senha igual Login, favor digite novamente!\n\n\n\n\n\n\n\n")

#________________________________________________________

'''
Exersise 3

3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento
'''
print("Supondo que a população de um país ....")
pais_a = 80000
pais_b = 200000
anos = 0
while True:
	pais_a+= (pais_a*.03)
	pais_b+= (pais_b*.015)
	anos+=1
	if pais_a >= pais_b:
		break
print(anos, "Anos \n\n\n\n\n\n\n\n")
	

'''
Exersise 4

4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

'''
qnt = int(input("Digite a qual valor Fibonacci requerido: "))
fibo_anterior = 0
fibo_atual = 1
fibo_nova = 0
for x in range(1,qnt):
		fibo_nova = fibo_anterior + fibo_atual
		fibo_anterior=fibo_atual
		fibo_atual=fibo_nova
print("F%d : %d"%(qnt,fibo_nova))
'''
Exersise 5

5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
'''
vlr_1 = int(input("Digite o primeiro valor para MDC: "))
vlr_2= int(input("Digite o segundo valor valor para MDC: "))
while True:
	if vlr_1%vlr_2 == 0:
		print ("MDC: %.0f \n\n\n\n\n\n\n\n" %(vlr_2))
		break
	else:
		x = vlr_1%vlr_2
		vlr_2 = x
	
