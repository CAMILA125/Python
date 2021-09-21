# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:10:27 2021

@author: Camila
"""

import numpy as np

print('Escolha seu treinamento: ' )
print('1 para: AND' )
print('2 para: OR' )
print('3 para: XOR' )

#iniciando os vetores com as possiveis entradas da rede
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#iniciando os pesos em 0 para deixar que a rede vá colocando os pesos
pesos = np.array([0.0, 0.0])
#taxa de apendizagem para ir reajustando os erros
taxaAprendizagem = 1

#função para passar o reusltado e saber se ativa o neurônio ou não
def funcaoStep(resultado):
    #neurônio é ativado apenas quando o valor da saida for 1 ou maior
	if(resultado >= 0):
		return 1
    #se não o neurônio não ativa
	return 0

	
#função para calcular as saidas 
def calcular(entrada,  bias, bias_peso):
    #faz cada entrada * cada peso
    u = entrada.dot(pesos) + (bias * bias_peso) #calculo da saida.
    #chama função que dicide se ativa ou não o resultado da entrada*peso
    return funcaoStep(u)
	
#iniciando o treinamento da rede
def treinamentoRede(loops):
    #inicializa ariaveis
    global taxaAprendizagem
    bias = 1
    bias_peso = 0
    totalErros = 1
    t = 0
    #executa até que o erro seja 0  ou até que sejam executados todos os loops pedidos
    while (totalErros != 0 and t<loops):
        #contabiliza loops
        t = t + 1
        totalErros = 0
        #percorremos todas as saidas da tabela verdade
        for i in range(len(saidas)):
            #temos um valor como saida para cada valor de entrada do array de entrada, transformando por exemplo [0,0] em ([0],[0])
            saidaObtida = calcular(np.asarray(entradas[i]), bias, bias_peso)
            #o erro é o valor que deveria ter saido na saida menos o valor que encontramos no calclo anterior
            erro = saidas[i] - saidaObtida
            if(erro != 0):
                
                print("b: ",bias)
                #percorremos todos os pesos do neurônio
                for j in range(len(pesos)):
                    #proximo pesso é igual a meu peso de agora + (a taxa de aprendizagem da ia * a minha entrada * o erro que encontrei anteriormente)
                    pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                    #apresento meu próximo peso
                    print('Peso atualizado: ' + str(pesos[j]))
                bias_peso = bias_peso + taxaAprendizagem * erro #calculo do bias conforme dado em aula.
            #somamos esse erro de cada saida no total do erro do array de saidas
            totalErros += erro        
        #após todos os calculos apresento o total de erros que a ia encontrou com os pesos aplicados
        print('Total de erros: ' + str(totalErros))
        
        #verfica se conseguiu treinar ou não 
    if totalErros == 0:
        print('Rede neural treinada com sucesso')
    else:
        print('Rede neural treinada com falhas')

#função para printar a saida escolhida
def printarSaida(entrada):
    print('saida')
    print(calcular(entrada))


#escolha do treinamento
treinamento = int(input('Digite:'))
#variavel que guarda a quantidade de loops a serem executados
loops = int(input('Digite a quantidade de loops:'))


if treinamento == 1:
#escolhido AND, aplica as saidas da tabela verdade do AND
    saidas = np.array([0,0,0,1])
    #chama o treinamento se tiver algum loop
    if loops > 0 :
        treinamentoRede(loops)
        #usuario digita um par de entradas para ver o que retornou
        n1 = int(input('Digite a entrada 1 com 0 ou 1:'))
        n2 = int(input('Digite a entrada 2 com 0 ou 1:'))
        #se for 0 ou 1 as entradas
        if (n1 == 0 or n1 == 1) and (n2 == 0 or n2 == 1):
            #printa uma saida que a rede treinou
            printarSaida( np.array([n1, n2]))
    else:
        print('A rede precisa de loops')
elif treinamento == 2:
#escolhido OR, aplica as saidas da tabela verdade do OR
    saidas = np.array([0,1,1,1])
    #chama o treinamento se tiver algum loop
    if loops > 0 :
        treinamentoRede(loops)
        #usuario digita um par de entradas para ver o que retornou
        n1 = int(input('Digite a entrada 1 com 0 ou 1:'))
        n2 = int(input('Digite a entrada 2 com 0 ou 1:'))
        #se for 0 ou 1 as entradas
        if (n1 == 0 or n1 == 1) and (n2 == 0 or n2 == 1):
            #printa uma saida que a rede treinou
            printarSaida( np.array([n1, n2]))
    else:
        print('A rede precisa de loops')
elif treinamento == 3:
#escolhido XOR, aplica as saidas da tabela verdade do XOR
    saidas = np.array([0,1,1,0])
    #chama o treinamento se tiver algum loop
    if loops > 0 :
        treinamentoRede(loops)
        #usuario digita um par de entradas para ver o que retornou
        n1 = int(input('Digite a entrada 1 com 0 ou 1:'))
        n2 = int(input('Digite a entrada 2 com 0 ou 1:'))
        #se for 0 ou 1 as entradas
        if (n1 == 0 or n1 == 1) and (n2 == 0 or n2 == 1):
            #printa uma saida que a rede treinou
            printarSaida( np.array([n1, n2]))
    else:
        print('A rede precisa de loops')
else:
#escolhido nenuma opção valida
    print('Digite um numero válido' )
