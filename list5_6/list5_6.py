#LISTA 5
Questão A. O que o seguinte programa (dado na forma de pseucódigo) imprime?
x = 2
y = 5
se y > 8 então
y = y * 2
caso contrário,
x = x * 2
imprime (x + y)
Resposta: 9
Questão B. Quantas vezes o trecho de pseudocódigo seguinte imprime 'oi'? (obs: na nossa pseudo-linguagem, o laço inclui os extremos, ou seja, 1 até 4 significa 1, 2, 3, 4.)
para i = 1 até 9
se i != 3, então
para j = 1 até 6
imprime 'oi'
Resposta: 48
Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também divisíveis por 7?
Resposta: 183
Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995
Questão E. Na pacata vila campestre de Ponteironuloville, todos os telefones têm 6 dígitos. A companhia telefônica estabelece as seguintes regras sobre os números:
1. Não pode haver dois dígitos consecutivos idênticos, porque isso é chato;
2. A soma dos dígitos tem que ser par, porque isso é legal;
3. O último dígito não pode ser igual ao primeiro, porque isso dá azar.
Então, dadas essas regras perfeitamente razoáveis, bem projetadas e maduras, quantos números de telefone na lista abaixo são válidos?
213752 216732 221063 221545 225583 229133 230648 233222 236043 237330 239636 240138 242123 246224 249183 252936 254711 257200 257607 261424 263814 266794 268649 273050 275001 277606 278997 283331 287104 287953 289137 291591 292559 292946 295180 295566 297529 300400 304707 306931 310638 313595 318449 319021 322082 323796 326266 326880 327249 329914 334392 334575 336723 336734 338808 343269 346040 350113 353631 357154 361633 361891 364889 365746 365749 366426 369156 369444 369689 372896 374983 375223 379163 380712 385640 386777 388599 389450 390178 392943 394742 395921 398644 398832 401149 402219 405364 408088 412901 417683 422267 424767 426613 430474 433910 435054 440052 444630 447852 449116 453865 457631 461750 462985 463328 466458 469601 473108 476773 477956 481991 482422 486195 488359 489209 489388 491928 496569 496964 497901 500877 502386 502715 507617 512526 512827 513796 518232 521455 524277 528496 529345 531231 531766 535067 535183 536593 537360 539055 540582 543708 547492 550779 551595 556493 558807 559102 562050 564962 569677 570945 575447 579937 580112 580680 582458 583012 585395 586244 587393 590483 593112 593894 594293 597525 598184 600455 600953 601523 605761 608618 609198 610141 610536 612636 615233 618314 622752 626345 626632 628889 629457 629643 633673 637656 641136 644176 644973 647617 652218 657143 659902 662224 666265 668010 672480 672695 676868 677125 678315
Resposta: 39

#LISA 6

#!/usr/bin/python -tt
# Exercícios by Nick Parlante (CodingBat)

# A. dormir
# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo quando é feriado ou não é dia semana
# retorne True ou False conforme você vá dormir ou não
def dormir(dia_semana, feriado):
  return 

# B. alunos_problema
# temos dois alunos a e b
# a_sorri e b_sorri indicam se a e b sorriem
# temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
# retorne True quando houver problemas
def alunos_problema(a_sorri, b_sorri):
  return 

# C. soma_dobro
# dados dois números inteiros retorna sua soma
# porém se os números forem iguais retorna o dobro da soma
# soma_dobro(1, 2) -> 3
# soma_dobro(2, 2) -> 8
def soma_dobro(a, b):
  return

# D. diff21
# dado um inteiro n retorna a diferença absoluta entre n e 21
# porém se o número for maior que 21 retorna dobro da diferença absoluta
# diff21(19) -> 2
# diff21(25) -> 8
# dica: abs(x) retorna o valor absoluto de x
def diff21(n):
  return 

# E. papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
  return

# F. dez
# dados dois inteiros a e b
# retorna True se um dos dois é 10 ou a soma é 10
def dez(a, b):
  return 

# G. dista10
# seja um inteiro n
# retorna True se a diferença absoluta entre n e 100 ou n e 200
# for menor ou igual a 10
# dista10(93) -> True
# dista10(90) -> True
# dista10(89) -> False
def dista10(n):
  return

# H. apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posição n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'
def apaga(s, n):
  return 

# I. troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  return

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Oba! Hoje vou ficar dormindo!')
  test(dormir(False, False), True)
  test(dormir(True, False), False)
  test(dormir(False, True), True)
  test(dormir(True, True), True)

  print ()
  print ('Alunos problema')
  test(alunos_problema(True, True), True)
  test(alunos_problema(False, False), True)
  test(alunos_problema(True, False), False)
  test(alunos_problema(False, True), False)

  print ()
  print ('Soma dobro')
  test(soma_dobro(1, 2), 3)
  test(soma_dobro(3, 2), 5)
  test(soma_dobro(2, 2), 8)
  test(soma_dobro(-1, 0), -1)
  test(soma_dobro(0, 0), 0)
  test(soma_dobro(0, 1), 1)

  print ()
  print ('Diff21')
  test(diff21(19), 2)
  test(diff21(10), 11)
  test(diff21(21), 0)
  test(diff21(22), 2)
  test(diff21(25), 8)
  test(diff21(30), 18)

  print ()
  print ('Papagaio')
  test(papagaio(True, 6), True)
  test(papagaio(True, 7), False)
  test(papagaio(False, 6), False)
  test(papagaio(True, 21), True)
  test(papagaio(False, 21), False)
  test(papagaio(True, 23), True)
  test(papagaio(True, 20), False)

  print ()
  print ('Dez')
  test(dez(9, 10), True)
  test(dez(9, 9), False)
  test(dez(1, 9), True)
  test(dez(10, 1), True)
  test(dez(10, 10), True)
  test(dez(8, 2), True)
  test(dez(8, 3), False)
  test(dez(10, 42), True)
  test(dez(12, -2), True)

  print ()
  print ('Dista 10')
  test(dista10(93), True)
  test(dista10(90), True)
  test(dista10(89), False)
  test(dista10(110), True)
  test(dista10(111), False)
  test(dista10(121), False)
  test(dista10(0), False)
  test(dista10(5), False)
  test(dista10(191), True)
  test(dista10(189), False)
  test(dista10(190), True)
  test(dista10(200), True)
  test(dista10(210), True)
  test(dista10(211), False)
  test(dista10(290), False)

  print ()
  print ('Apaga')
  test(apaga('kitten', 1), 'ktten')
  test(apaga('kitten', 0), 'itten') 
  test(apaga('kitten', 4), 'kittn')
  test(apaga('Hi', 0), 'i')
  test(apaga('Hi', 1), 'H')
  test(apaga('code', 0), 'ode')
  test(apaga('code', 1), 'cde')
  test(apaga('code', 2), 'coe')
  test(apaga('code', 3), 'cod')
  test(apaga('chocolate', 8), 'chocolat')

  print ()
  print ('Troca letras')
  test(troca('code'), 'eodc')	    
  test(troca('a'), 'a')
  test(troca('ab'), 'ba')
  test(troca('abc'), 'cba')
  test(troca(''), '')
  test(troca('Chocolate'), 'ehocolatC')
  test(troca('nythoP'), 'Python')
  test(troca('hello'), 'oellh')
  
if __name__ == '__main__':
  main()
