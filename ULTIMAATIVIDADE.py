# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:08:32 2021

@author: Camila
"""

import random
populacaoNova = []

def eletismo(pai1,pai2):
    global populacaoNova
    populacaoNova.append(pai1)
    populacaoNova.append(pai2)

# função para passar o reusltado e saber se ativa o neurônio ou não
def girarRoleta():
    global populacaoNova
    populacaoNova = []
    somaParcial = 0
    posicao = []
    for i in range(len(aptidao)):
        
        posicao.append([somaParcial,aptidao[i]])
        somaParcial = somaParcial + aptidao[i] 
        
    intervalo = sum(aptidao)
    v1 =random.randrange(0,intervalo)
    v2 =random.randrange(0,intervalo)
    for i in range(len(posicao)):
        inicial=posicao[i][0]
        final=(posicao[i][0])+(posicao[i][1])
        lista = list(range(inicial,final))
        if v1 in lista:
            pai1 = populacao[i]
        if v2 in lista:
            pai2 = populacao[i]
    print(pai1," ",pai2)
    criacao = cruzamento(pai1,pai2)
    mutante1 = mutacao(criacao[0],escolherM)
    mutante2 = mutacao(criacao[1],escolherM)
    populacaoNova.append(mutante1)
    populacaoNova.append(mutante2)
    
# função para passar o reusltado e saber se ativa o neurônio ou não
def mutacao(filho,escolherM):
    sorteio = random.randrange(0,99)
    if sorteio <= escolherM :
        posicaoAleatoria =random.randrange(0,9)
        if filho[posicaoAleatoria] == 0:
            filho[posicaoAleatoria] = 1
             
        elif filho[posicaoAleatoria] == 1:
             filho[posicaoAleatoria] = 0
    return filho
# função para passar o reusltado e saber se ativa o neurônio ou não
def cruzamento(pai1,pai2):

    corte =random.randrange(1,9)
    filho1=pai1[:corte]+pai2[corte:]
    filho2=pai2[corte:]+pai1[:corte]
    
    return [filho1,filho2]
    

cromossomo = []
quantidade = 10
aptidao = []
Q= 1
while Q > 0:
    capacidade = int(input("Digite a capacidade da mochila de 15 a 20: " ))
    if capacidade >14 and capacidade<21:
        print("Valor válido." )
        break
    else:
        print("Valor inválido." )
        
    
while quantidade > len(cromossomo):
    peso = int(input("Digite o peso do item: " ))
    valor = int(input("Digite o valor do item: " ))
    i=[peso,valor]
    if i not in cromossomo:
        cromossomo.append(i)
    else:
        print("item já existe, não foi cadastrado" )
cromossomo = []
quantidadesBolsa = []
capacidade=50
eletismoEscolhido = int(input("Digite 1 para ativar e 0 para desativar o eletismo: " ))
Tpopulacao = int(input("Digite o tamanho inicial da população: " ))
geracoes = int(input("Digite o valor máximo de gerações: " ))

escolherM = int(input("Digite um numero maior que 0 para taxa de mutação caso seja 0 o sistema irá fazer automaticamente o calculo: " ))
populacao = [[[1,2],[3,4],[5,6],[7,8],[9,1],[2,3],[4,5],[6,7],[8,9],[2,6]],
             [[1,2],[3,4],[5,6],[7,8],[9,1],[2,3],[4,5],[6,7],[8,9],[2,6]],
             [[1,2],[3,4],[5,6],[7,8],[9,1],[2,3],[4,5],[6,7],[8,9],[2,6]]]



for i in range(len(populacao)):
    cromossomo = populacao[i]
    total = sum(map(lambda x: int(x[0]), cromossomo))
    if eletismoEscolhido == 1:
        quantidadesBolsa.append(sum(map(lambda x: int(x[3]), cromossomo)))
        melhorcromossomo = max(quantidadesBolsa)
        n_pos = quantidadesBolsa.index(melhorcromossomo) 
        quantidadesBolsa.pop(n_pos)
        melhorcromossomo = max(quantidadesBolsa)
        eletismo(melhorcromossomo,melhorcromossomo)
        print(total)
    if total <= capacidade:
        aptidao.append(sum(map(lambda x: int(x[1]), cromossomo)))
    
print(aptidao)

if escolherM == 0:          
    escolherM=((Tpopulacao*quantidade)** (1/2)) ** (-1)

temp=0
while(temp<= geracoes):
    temp = temp + 1

    while(len(populacao)> len(populacaoNova)):
        girarRoleta()


 

