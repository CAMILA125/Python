# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:10:27 2021

@author: Camila
"""

print('Escolha seu treinamento: ')
print('1 para: AND')
print('2 para: OR')
print('3 para: XOR')

#iniciando os vetores com as possiveis entradas da rede
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
#iniciando os pesos em 0 para deixar que a rede vá colocando os pesos
pesos = [0.0, 0.0]
#pesso do bias
bias_peso = 0
#taxa de apendizagem para ir reajustando os erros
taxaAprendizagem = 1


# função para passar o reusltado e saber se ativa o neurônio ou não
def funcaoStep(resultado):
    # neurônio é ativado apenas quando o valor da saida for 0 ou maior
    if (resultado >= 0):
        return 1
    # se não o neurônio não ativa
    return 0


# função para calcular as saidas
def calcular(entradas):
    #bias sempre é 1
    bias = 1
    #pesso do bias calculado ao longo do treinamento
    global bias_peso
    # faz cada entrada * cada peso + bias* pesso do bias
    u = (entradas[0] * pesos[0]) + (entradas[1] * pesos[1]) + (bias * bias_peso)
    # chama função que dicide se ativa ou não com o resultado anterior
    return funcaoStep(u)


#iniciando o treinamento da rede
def treinamentoRede(loops):
    # inicializa variaveis
    erro = 1
    teveE = 1
    t = 0
    # executa até que o loop tenha erro = 0  ou até que sejam executados todos os loops pedidos
    while (teveE != 0 and t < loops):
        # contabiliza loops
        t = t + 1
        erro = 0
        teveE = 0
        global bias_peso
        # percorremos todas as saidas da tabela verdade
        for i in range(len(saidas)):
            # calculamos uma saida para as cada par de entrada
            saidaObtida = calcular(entradas[i])
            # o erro é o valor que deveria ter saido na saida menos o valor que encontramos no calclo anterior
            erro = saidas[i] - saidaObtida
            print('Erro: ' + str(erro))
            # caso tenha algun erro atualiza os pesos.
            if erro != 0:
                # percorremos todos os pesos do neurônio
                for j in range(len(pesos)):
                    # proximo pesso é igual a meu peso de agora + (a taxa de aprendizagem da ia * a minha entrada * o erro que encontrei anteriormente)
                    pesos[j] = pesos[j] + taxaAprendizagem * erro * entradas[i][j]
                    print('Peso atualizado: ' + str(pesos[j]))
                teveE = teveE + 1
                # calcula o bias sendo seu pesso atual + a taxa de aprendizagem da ia * o erro que encontrei anteriormente
                bias_peso = bias_peso + taxaAprendizagem * erro
                print('Peso do bias atualizado: ' + str(bias_peso))
        pass
    pass
    if teveE == 0:
        print('Rede neural treinada com sucesso')
    else:
        print('Rede neural treinada com falhas')


# função para printar a saida escolhida pelo usuario
def printarSaida(entrada):
    print('saida')
    print(calcular(entrada))



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
else:
    # escolhido nenuma opção valida
    print('Digite um numero válido')


