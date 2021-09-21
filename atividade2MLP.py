# -*- coding: utf-8 -*-
"""
@author: Bruno
"""

import math

entradas = [[0,0],[0,1],[1,0],[1,1]]

pesos = [
    [0.0,0.0], # 0 - Neuronio A entradas
    [0.0,0.0], # 1 - Neuronio B entradas
    [0.0,0.0]  # 2 - Neuronio C entradas
    ]

bias = 0
bias_peso = [0.0,0.0,0.0] # 0 - A / 1 - B / 2 - C

taxa_de_treino = 0.5

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
    [1,1,1,0], # 2 - NAND
    [1,0,0,0], # 3 - NOR
    [0,1,1,0]  # 4 - XOR
]

print()

#função de treinamento
def treinamento():
    erro = 1 #total de erros
    teveE = 1
    
    rx = 1
    for m in range(3):
        for n in range(2):
            pesos[m][n] = rx
    
    
    while(teveE != 0):
        erro = 0
        teveE = 0
        global bias_peso
        
        for i in range(4): #testar as 4 entradas.
            s = [0,0,0] # 0 - A / 1 - B / 2 - C
            a = [0,0,0] #ativação de a, b e c
            for j in range(2):
                a[j] = bias_peso[j] * bias + pesos[j][0] * entradas[i][0] + pesos[j][1] * entradas[i][1]
                s[j] = 1 / (1 + math.exp(-a[j]))
            
            a[2] = bias_peso[2] * bias + s[0] * pesos[2][0] + bias + s[1] * pesos[2][1]
            s[2] = 1 / (1 + math.exp(-a[2]))
            
            if s[2] >= 0:
                s[2] = 1
            else:
                s[2] = 0
            
            erro = saida_esperada[ttreino][i] - s[2]
            
            if erro != 0: 
                erros = [0.0,0.0,0.0] # 0 - A / 1 - B / 2 - C
                erros[2] = erro * s[2] * (1-s[2])
                
                for k in range(2):
                    erros[k] = s[k] * (1-s[k]) * pesos[2][k] * erros[2]
                    for h in range(2):
                        pesos[k][h] = pesos[k][h] + (taxa_de_treino * erros[k] * entradas[i][h])
                        pass
                    bias_peso[k] = bias_peso[k] * (taxa_de_treino * erros[k] * bias)
                    pass
                
                bias_peso[2] = (taxa_de_treino * erros[2] * bias)
                for g in range(2):
                    pesos[2][g] = (taxa_de_treino * erros[2] * s[g])
                
                
            
        pass
    
    pass

print("escolha a porta desejada para o treinamento:")
print("0-AND")
print("1-OR")
print("2-NAND")
print("3-NOR")
print("4-XOR")

ttreino = int(input())

treinamento()

print(pesos)
print(bias_peso)

testInputs = [0,0]

e1 = int(input())
e2 = int(input())

s = [0,0,0] # 0 - A / 1 - B / 2 - C
a = [0,0,0] #ativação de a, b e c
for j in range(2):
    a[j] = bias_peso[j] * bias + pesos[j][0] * e1 + pesos[j][1] * e2
    s[j] = 1 / (1 + math.exp(-a[j]))
    pass
a[2] = bias_peso[2] * bias + s[0] * pesos[2][0] + bias + s[1] * pesos[2][1]
s[2] = 1 / (1 + math.exp(-a[2]))
    
if s[2] >= 0.0:
    print(1)
else:
    print(0)
            




























