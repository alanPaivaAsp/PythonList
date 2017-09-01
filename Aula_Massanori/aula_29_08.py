#Calcule a some de números inteiros até ser digitado zero

soma=0
cont=0
while True:
   x = int(input("Digite o numero (0 sai) :"))
   if x==0:
    break
   soma+= x
   cont += 1
media = soma/cont
print ("Soma e: ", soma)
print("Media da soma e: ", media)



# Faça a tabuada do 1 ao 10

x=1
y=1
while x<11:
  print("Tabuada do %d"%x)
  while y<11:
    print("%d x %d : %d" %(x,y,(x*y)))
    y+=1
  x+=1
  y=1 