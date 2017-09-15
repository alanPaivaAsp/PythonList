'''
1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
'''
from random import randint
maior_menor = list()
num = list()
maior_menor.extend([0,101])
#Recebe o array (num) e calcula o maior e o menor retornando os valores menor e maior em um array 
def verifica_valor(nums):
	for x in range (0,10):
		if nums[x] >=maior_menor[0]:
			maior_menor[0] =nums[x]
		elif nums[x]<= maior_menor[1]:
			maior_menor[1] =nums[x]
	return 	maior_menor
#___________________	
#Gerando os 10 valores aleatórios e colocando num array
def create_rand(num,x):
	for y in range(0,x):
		num.append(randint(1,100))
#___________________		
#usando a função para verificar o maior e o menor,então printar
create_rand(num,10)
maior_menor = verifica_valor(num)
print("10 Valores Ex. 1: ",num)
print("Maior e menor, respectivamente", maior_menor ," \n\n\n\n\n\n\n\n\n\n\n\n")
'''	
2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.
'''
num = list()
par = list()
impar = list()
#função para jogar cada valor para seu devido array impar ou par
def valida_par_impar(num,x):
	for y in range(x):
		if num[y]%2==0:
			par.append(num[y])
		elif num[y]%2 != 0:
			impar.append(num[y])
#reaproveitando a função da linha 18
create_rand(num,20)
valida_par_impar(num,20)
#printando os arrays
print("20 VALORES EX. 2: ", num)
print("Par: ",par)
print("Impar: ",impar ,"\n\n\n\n\n\n\n\n\n\n")


'''
3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.
'''
def intercala (vet1,vet2,vet3,x):
	cont_1 = 0
	cont_2 = 0
	
	for y in range(x):
		if y%2==0:
			vet3.append(vet1[cont_1])
			cont_1+=1
		elif y%2!=0:
			vet3.append(vet2[cont_2])
			cont_2+=1
	



vet1 = list()
vet2 = list()
vet3 = list()
create_rand(vet1,10)
create_rand(vet2,10)
intercala(vet1,vet2,vet3,20)
print ("Primeira lista EX3: ",vet1)
print ("Segunda lista: ",vet2)
print ("Lista intercalada: ",vet3,"\n\n\n\n\n\n\n\n\n\n\n\n")



'''
4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
'''
x = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
x= x.replace("."," ")
x= x.replace(","," ")
x= x.replace(":"," ")
words = list()
words = x.split()
words_py = list()
for y in range (len(words)):
	if words[y].startswith('p') or words[y].startswith('y') or words[y].startswith('t') or words[y].startswith('h')or words[y].startswith('o') or words[y].startswith('n'):
		words_py.append(words[y])
	elif words[y].endswith('p') or words[y].endswith('y') or words[y].endswith('t') or words[y].endswith('h') or words[y].endswith('o') or words[y].endswith('n'):
		words_py.append(words[y])
print (words_py)

print ("\n\n\n\n\n\n\n\n\n\n\n\n\n")

'''
5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
'''	
x = x.lower()
words = list()
words = x.split()
words_py = list()
for y in range (len(words)):
	if words[y].startswith('p') or words[y].startswith('y') or words[y].startswith('t') or words[y].startswith('h')or words[y].startswith('o') or words[y].startswith('n'):
		if len(words[y])> 4:
			words_py.append(words[y])
	elif words[y].endswith('p') or words[y].endswith('y') or words[y].endswith('t') or words[y].endswith('h') or words[y].endswith('o') or words[y].endswith('n'):
			if len(words[y])> 4:
				words_py.append(words[y])
				
print (words_py)
	
	