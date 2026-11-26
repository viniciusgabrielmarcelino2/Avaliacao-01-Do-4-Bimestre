################################################################################
# Descrição: Elaborar um programa que leia uma matriz A de uma dimensão com    #
#            dez elementos numéricos inteiros. Apresentar o total de elementos #
#            ímpares existentes na matriz e o percentual do valor total de     #
#            números ímpares em relação à quantidade total de elementos        #
#            armazenados na matriz.                                            #
# Parâmetros de entrada: 10 números inteiros.                                  #
# Valores de saída: Quantidade de números ímpares e seu percentual em relação  #
#                   aos 10 elementos.                                          #
# Autor: Vinicius Gabriel Marcelino Maciel                                     #
################################################################################

vetor_a = []
for indice in range(10):
    vetor_a.append(int(input(f"A[{indice}]: ")))

impares = 0
for valor in vetor_a:
    if valor % 2 != 0:
        impares += 1

percentual = 100 * impares / len(vetor_a)
print(f"Quantidade de ímpares: {impares}")
print(f"Percentual de ímpares: {percentual:g}%")
