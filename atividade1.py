# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:10:58 2021

@author: Bruno
"""

"""
não sei se eu que entendi errado ou se só não sei usar python mesmo.
bom pelo menos vou enviar isso aqui.
"""

entradas = [[0,0],[0,1],[1,0],[1,1]]

pesos = [0.0,0.0]

bias_peso = 0

taxa_de_treino = 1

ttreino = 0
#saidas esperadas.
saida_esperada = [
    #ordem dentro da array
    # 0 | 0 | [0]
    # 0 | 1 | [1]
    # 1 | 0 | [2]
    # 1 | 1 | [3]
    
    [0,0,0,1], # 0 - AND
    [0,1,1,1], # 1 - OR
    [0,1,1,0]  # 3 - XOR
]

#função de treinamento
def treinamento():
    erro = 1 #total de erros
    teveE = 1
    
    while(teveE != 0):
        erro = 0
        teveE = 0
        bias = 1
        global bias_peso
        for i in range(4): #testar as 4 entradas.
            s = (entradas[i][0] * pesos[0]) + (entradas[i][1] * pesos[1]) + (bias * bias_peso) #calculo da saida.
            if s >= 0:
                s = 1
            else:
                s = 0
            
            erro = saida_esperada[ttreino][i] - s #calculo do erro conforme dado em aula.
            print(erro)
            if erro != 0: #caso tenha algun erro atualiza os pesos.
                for j in range(2): 
                    pesos[j] = pesos[j] + taxa_de_treino * erro * entradas[i][j] #calculo do peso conforme dado em aula.
                teveE = teveE + 1
                bias_peso = bias_peso + taxa_de_treino * erro #calculo do bias conforme dado em aula.
            
        pass
    
    pass
    
print("escolha a porta desejada para o treinamento:")
print("0-AND")
print("1-OR")
print("2-XOR")

ttreino = int(input())

treinamento()

print(pesos)
print(bias_peso)

testInputs = [0,0]

testInputs[0] = int(input())
testInputs[1] = int(input())

if (testInputs[0] * pesos[0]) + (testInputs[1] * pesos[1]) + (1 * bias_peso) >= 0:
    print("1")
else:
    print("0")




























