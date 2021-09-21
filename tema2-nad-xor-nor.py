# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:10:27 2021

@author: Camila
"""
import math
import random
print('Escolha seu treinamento: ')
print('1 para: AND')
print('2 para: OR')
print('3 para: XOR')
print('4 para: NOR')
print('5 para: NAND')

#iniciando os vetores com as possiveis entradas da rede
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
#iniciando os pesos dos neurônios com pesos aleatórios entre -1.2 e 1.2
a0 =random.uniform(-1.2, 1.2)
b0 =random.uniform(-1.2, 1.2)
c0 =random.uniform(-1.2, 1.2)
a1 =random.uniform(-1.2, 1.2)
b1 =random.uniform(-1.2, 1.2)
c1 =random.uniform(-1.2, 1.2)
pesos = [[a0, a1],[b0,b1],[c0,c1]]
#pesso do bias com pesos aleatórios entre -1.2 e 1.2
ba =random.uniform(-1.2, 1.2)
bb =random.uniform(-1.2, 1.2)
bc =random.uniform(-1.2, 1.2)
bias_peso = [ba, bb, bc]
#taxa de apendizagem para ir reajustando os erros
taxaAprendizagem = 1


# função para passar o reusltado e saber se ativa o neurônio ou não
def funcaoStep(resultado):
    # neurônio é ativado apenas quando o valor da saida for 0.5 ou maior
    if (resultado >= 0.5):
        return 1
    # se não o neurônio não ativa
    return 0


# função para calcular as saidas
def calcular(entradas,pesos,bias_peso):
    #bias sempre é 1
    bias = 1
    #pesso do bias calculado ao longo do treinamento
    # faz cada entrada * cada peso + bias* pesso do bias
    u = (entradas[0] * pesos[0]) + (entradas[1] * pesos[1]) + (bias * bias_peso)
    #fução para o calculo já pre estabelecida
    return (1/(1 + math.exp(-u )))

# função para calcular os pesos
def calcularPeso(entradas, erros,k):
    
    #bias sempre é 1
    global taxaAprendizagem
    bias = 1
    # atualiza pesso é igual a meu peso de agora + (a taxa de aprendizagem da ia  * o erro que encontrei anteriormente * a minha entrada)
    pesos[k][0] = pesos[k][0] + (taxaAprendizagem * erros * entradas[0])
    # atualiza pesso é igual a meu peso de agora + (a taxa de aprendizagem da ia  * o erro que encontrei anteriormente * a minha entrada)
    pesos[k][1] = pesos[k][1] + (taxaAprendizagem * erros * entradas[1])
    print('Peso atualizado: ' + str(pesos[k]))
    #pesso do bias calculado ao longo do treinamento
    bias_peso[k] = bias_peso[k] + (taxaAprendizagem * erros * bias)
    print('Peso do bias atualizado: ' + str(bias_peso[k]))

#iniciando o treinamento da rede
def treinamentoRede(loops):
    # inicializa variaveis
    erros = [0,0,0]
    teveE = 1
    t = 0
    # executa até que o loop tenha erro = 0  ou até que sejam executados todos os loops pedidos
    while (teveE != 0 and t < loops):
        # contabiliza loops
        t = t + 1
        teveE = 1
        global bias_peso
        # percorremos todas as saidas da tabela verdade
        for i in range(len(saidas)):
            # calculamos uma saida para as cada par de entrada
            saidaObtida0 = calcular(entradas[i],pesos[0],bias_peso[0])
            saidaObtida1 = calcular(entradas[i],pesos[1],bias_peso[1])
            saidaObtida2 = funcaoStep(calcular([saidaObtida0,saidaObtida1],pesos[2],bias_peso[2]))
            print("saida obtida",saidaObtida2)
            # o erro é o valor que deveria ter saido na saida menos o valor que encontramos no calclo anterior
            erroGeral = saidas[i] - saidaObtida2
            print('Erro geral: ' + str(erroGeral))
            # caso tenha algun erro atualiza os pesos.
            if erroGeral != 0 :
                #faz a FASE BACKWARD
                erros[2] = erroGeral * saidaObtida2 * (1-saidaObtida2)
                erros[1] = saidaObtida1 * (1-saidaObtida1 ) * pesos[2][1] * erros[2]
                erros[0] = saidaObtida0 * (1-saidaObtida0 ) * pesos[2][0] * erros[2]
                
                #atualiza os pesos de cada neurônio
                calcularPeso(entradas[i], erros[0], 0)
                calcularPeso(entradas[i], erros[1], 1)
                calcularPeso([saidaObtida0,saidaObtida1], erros[2], 2)
        pass
    pass
    if teveE == 0:
        print('Rede neural treinada com sucesso')
    else:
        print('Rede neural treinada com falhas')


# função para printar a saida escolhida pelo usuario
def printarSaida(entrada):
    print('saida')
    # calculamos uma saida para o par de entrada escolhido pelo usuario
    #passagem pelo neurônio a
    saidaObtida0 = calcular(entrada,pesos[0],bias_peso[0])
    #passagem pelo neurônio b
    saidaObtida1 = calcular(entrada,pesos[1],bias_peso[1])
    #passagem pelo neurônio c
    saidaObtida2 = funcaoStep(calcular([saidaObtida0,saidaObtida1],pesos[2],bias_peso[2]))
    print("Saida",saidaObtida2)



# escolha do treinamento
treinamento = int(input('Digite:'))
# variavel que guarda a quantidade de loops a serem executados
loops = int(input('Digite a quantidade de loops:'))

if treinamento == 1:
    # escolhido AND, aplica as saidas da tabela verdade do AND
    saidas = [0, 0, 0, 1]
    # chama o treinamento se tiver algum loop
    if loops > 0:
        treinamentoRede(loops)
        # printa os pesos dos neurônios e o peso do bias após o treinameto
        print("Pessos finais: ",pesos)
        print("Pesso do bias final",bias_peso)
        # usuario digita um par de entradas para ver o que retornou
        n1 = int(input('Digite a entrada 1 com 0 ou 1:'))
        n2 = int(input('Digite a entrada 2 com 0 ou 1:'))
        # se for 0 ou 1 as entradas
        if (n1 == 0 or n1 == 1) and (n2 == 0 or n2 == 1):
            # printa uma saida que a rede treinou
            printarSaida([n1, n2])
    else:
        print('A rede precisa de loops')
elif treinamento == 2:
    # escolhido OR, aplica as saidas da tabela verdade do OR
    saidas = [0, 1, 1, 1]
    # chama o treinamento se tiver algum loop
    if loops > 0:
        treinamentoRede(loops)
        # printa os pesos dos neurônios e o peso do bias após o treinameto
        print(pesos)
        print(bias_peso)
        # usuario digita um par de entradas para ver o que retornou
        n1 = int(input('Digite a entrada 1 com 0 ou 1:'))
        n2 = int(input('Digite a entrada 2 com 0 ou 1:'))
        # se for 0 ou 1 as entradas
        if (n1 == 0 or n1 == 1) and (n2 == 0 or n2 == 1):
            # printa uma saida que a rede treinou
            printarSaida([n1, n2])
    else:
        print('A rede precisa de loops')
elif treinamento == 3:
    # escolhido XOR, aplica as saidas da tabela verdade do XOR
    saidas = [0, 1, 1, 0]
    # chama o treinamento se tiver algum loop
    if loops > 0:
        treinamentoRede(loops)
        # printa os pesos dos neurônios e o peso do bias após o treinameto
        print(pesos)
        print(bias_peso)
        # usuario digita um par de entradas para ver o que retornou
        n1 = int(input('Digite a entrada 1 com 0 ou 1:'))
        n2 = int(input('Digite a entrada 2 com 0 ou 1:'))
        # se for 0 ou 1 as entradas
        if (n1 == 0 or n1 == 1) and (n2 == 0 or n2 == 1):
            # printa uma saida que a rede treinou
            printarSaida([n1, n2])
    else:
        print('A rede precisa de loops')
elif treinamento == 4:
    # escolhido NOR, aplica as saidas da tabela verdade do NOR
    saidas = [1, 0, 0, 0]
    # chama o treinamento se tiver algum loop
    if loops > 0:
        treinamentoRede(loops)
        # printa os pesos dos neurônios e o peso do bias após o treinameto
        print(pesos)
        print(bias_peso)
        # usuario digita um par de entradas para ver o que retornou
        n1 = int(input('Digite a entrada 1 com 0 ou 1:'))
        n2 = int(input('Digite a entrada 2 com 0 ou 1:'))
        # se for 0 ou 1 as entradas
        if (n1 == 0 or n1 == 1) and (n2 == 0 or n2 == 1):
            # printa uma saida que a rede treinou
            printarSaida([n1, n2])
    else:
        print('A rede precisa de loops')
elif treinamento == 5:
    # escolhido NAND, aplica as saidas da tabela verdade do NAND
    saidas = [1, 1, 1, 0]
    # chama o treinamento se tiver algum loop
    if loops > 0:
        treinamentoRede(loops)
        # printa os pesos dos neurônios e o peso do bias após o treinameto
        print(pesos)
        print(bias_peso)
        # usuario digita um par de entradas para ver o que retornou
        n1 = int(input('Digite a entrada 1 com 0 ou 1:'))
        n2 = int(input('Digite a entrada 2 com 0 ou 1:'))
        # se for 0 ou 1 as entradas
        if (n1 == 0 or n1 == 1) and (n2 == 0 or n2 == 1):
            # printa uma saida que a rede treinou
            printarSaida([n1, n2])
    else:
        print('A rede precisa de loops')
else:
    # escolhido nenuma opção valida
    print('Digite um numero válido')


