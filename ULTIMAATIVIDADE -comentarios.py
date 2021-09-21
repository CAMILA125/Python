# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:08:32 2021

@author: Camila
"""

import random
populacaoNova = []

#função para fazer o eletismo
def eletismo(pai1,pai2):
    print("entrou eletismo")
    global populacaoNova
    #aducuina os 2 pais como os 2 primeiros filhos da nova geração
    populacaoNova.append(pai1)
    populacaoNova.append(pai2)
    print("saiu eletismo")

# função  para girar a roleta e criar 2 filhos para a próxima população
def girarRoleta():
    print("entrou roleta")
    global populacaoNova
    populacaoNova = []
    somaParcial = 0
    posicao = []
    global aptidao
    print("aptidao: ",aptidao)
    #Percorre todas as aptidões para poder popular o array posição com o tamanho e onde começa as posiçõe na roleta
    for i in range(len(aptidao)):
        posicao.append([somaParcial,aptidao[i]])
        somaParcial = somaParcial + aptidao[i] 
    #faz a soma de todas as aptidoes para saber o  tamanho que deve ter a roleta
    intervalo = sum(aptidao)
    #sorteia 2 numeros inteiros dentro do tamanho da roleta
    v1 =random.randrange(0,intervalo)
    v2 =random.randrange(0,intervalo)
    #percorre todas as posições do arrey que contem o tamanho de cada pedaço e onde inicia esse pedaço na roleta
    for i in range(len(posicao)):
        #valor inicial
        inicial=posicao[i][0]
        #valor final da posiçãp
        final=(posicao[i][0])+(posicao[i][1])
        #monta uma lista que vai por exempro do 10 ao 20
        lista = list(range(inicial,final))
        #faz a verificação se o primeiro valor sorteado está dentro da lista que possui os valores daquela posição da roleta se sim: escolhe o cromossomo
        if v1 in lista:
            pai1 = populacao[i]
        #faz a verificação se o segundo valor sorteado está dentro da lista que possui os valores daquela posição da roleta se sim: escolhe o cromossomo
        if v2 in lista:
            pai2 = populacao[i]
    print("pai1: ",pai1," ","pai2: ",pai2)
    #chama a função mutação
    criacao = cruzamento(pai1,pai2)
    #chma a função mutação para os 2 filhos que surgiram do cruzamento
    mutante1 = mutacao(criacao[0],escolherM)
    mutante2 = mutacao(criacao[1],escolherM)
    #coloca na nova população os 2 novos filhos
    populacaoNova.append(mutante1)
    populacaoNova.append(mutante2)
    print("saiu roleta")
    
# função para fazer a mutação
def mutacao(filho,escolherM):
    print("entrou mutacao")
    #faz o sorteio de um numero de 0 a 99% 
    sorteio = random.randrange(0,99)
    # verifica se o valor sorteado  é menor que o valor escolhido  da taxa de mutação
    if sorteio <= escolherM :
        #se for escolhe um valor aleatório para escolher a posição do cromossomo que vai mudar de 0 para 1 ou de 1 para 0
        posicaoAleatoria =random.randrange(0,9)
        if filho[posicaoAleatoria] == 0:
            filho[posicaoAleatoria] = 1
             
        elif filho[posicaoAleatoria] == 1:
             filho[posicaoAleatoria] = 0
    print("saiu mutacao")
    return filho
# função para fazer o cruzamento de 3 pais e retornar 2 novos filhos
def cruzamento(pai1,pai2):
    print("entrou cruzamento")
    #sorteia um valor aleatório de 1 a 9 para que tenha pelo menos 1 corte no cromossoma 
    corte =random.randrange(1,9)
    #filho 1 é igual ao primeiro pedaço do cromossomo pai1 até o corte e a segunda parte do cromossomo pai2 do corte até o final dele
    filho1=pai1[:corte]+pai2[corte:]
    #filho 2 é igual ao segundo pedaço do cromossomo pai2  ou seja do corte até o final dele e a primeira parte do cromossomo pai1 do inicio até o corte
    filho2=pai2[corte:]+pai1[:corte]
    print("saiu cruzamento")
    return [filho1,filho2]
    

quantidade = 10
aptidao = []
item = []

Q= 1
#fica no loop até digitar um valor que seja maior que 14 e menor que 21, caso seja sai do loop
while Q > 0:
    #usuario digita a capacidade
    capacidade = int(input("Digite a capacidade da mochila de 15 a 20: " ))
    if capacidade >14 and capacidade<21:
        print("Valor válido." )
        break
    else:
        print("Valor inválido." )
        
#faz o loop até que  o tamanhodo cromossomo seja igual ao da quantidade de itens que precisa
while quantidade > len(item):
    #usuario digita o peso e o valor do seu item
    peso = int(input("Digite o peso: " ))
    valor = int(input("Digite o valor: " ))
    i=[peso,valor]
    #se não existe um item igual a ele, o item é acrescentado ao cromossomo
    if i not in item:
        item.append(i)
    else:
        print("item já existe, não foi cadastrado" )

cromossomo = []
quantidadesBolsa = []
populacao = []
capacidade=50
#usuario escolhe se quer eletismo
eletismoEscolhido = int(input("Digite 1 para ativar e 0 para desativar o eletismo: " ))
#usuario escolhe tamanho inicial da população
Tpopulacao = int(input("Digite o tamanho inicial da população: " ))
#usuario escolhe quantas gerações vai querer
geracoes = int(input("Digite o valor máximo de gerações: " ))

#usuario escolhe a taxa de mutação
escolherM = int(input("Digite um numero maior que 0 para taxa de mutação caso seja 0 o sistema irá fazer automaticamente o calculo: " ))

if not (Tpopulacao%2) == 0:
    Tpopulacao = Tpopulacao + 1
print(Tpopulacao)
for i in range(Tpopulacao):
    cromossomo = []
    for j in range(10):
        a = random.randrange(0,2)
        #se for escolhe um valor aleatório para escolher a posição do cromossomo que vai mudar de 0 para 1 ou de 1 para 0
        cromossomo.append(a)
    populacao.append(cromossomo)


print("populacao inicial: ",populacao)


#caso o usuario não tenha escolhido uma taxa  o sistema calcula pela formula sugerida
if escolherM == 0:          
    escolherM=((Tpopulacao*quantidade)** (1/2)) ** (-1)


#Faz um loop para cada geração
temp=0
while(temp<= geracoes):
    temp = temp + 1
    #percorre a população
    for i in range(len(populacao)):
        #cada vetor da população é um cromossomo
        cromossomo = populacao[i]
        totalPeso = 0
        totalAptidao = 0
        for i in range(len(cromossomo)):
            #faz o total do pesso dos itens que foi calclado para estar na mochila
            if cromossomo[i] == 1:
                totalPeso = totalPeso + item[i][0]
        #faz uma lista com a quantidade de itens que tem o cromossomo
        quantidadesBolsa.append(sum(cromossomo))
        print(totalPeso)
        #se o total do cromossomo for menor ou igual a capacidade da mochila significa que é um comossomo validao
        if totalPeso <= capacidade:
            for i in range(len(cromossomo)):
                #soma a aptidão do item, ou seja soma todos os valores da mochila
                if cromossomo[i] == 1:
                    totalAptidao = totalAptidao + item[i][1]
            aptidao.append(totalAptidao)       


    print(aptidao)
    #se o usuario escolheu o eletismo     
    if eletismoEscolhido == 1:
        comossomoM1=max(quantidadesBolsa)
        quantidadesBolsa.remove(max(quantidadesBolsa))
        cromossomoM2 = max(quantidadesBolsa)
        #chama a função eletismo passando os 2 melhores cromossomos
        eletismo(comossomoM1,cromossomoM2)
    #gira a roleta para popular a nova população até que ela tenha o tamanho da antiga
    while(len(populacao)> len(populacaoNova)):
        girarRoleta()

    populacao = populacaoNova 

 

