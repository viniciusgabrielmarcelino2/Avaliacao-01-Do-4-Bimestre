################################################################################
# Descrição: Elaborar um programa que leia 15 elementos reais para uma matriz  #
#            A de uma dimensão do tipo vetor. Construir uma matriz B de mesmo  #
#            tipo e dimensão, observando a seguinte lei de formação: "todo     #
#            elemento da matriz A que possuir índice par deve ter seu elemento #
#            dividido por 2; caso contrário, o elemento da matriz A deve ser   #
#            multiplicado por 1.5". Apresentar os elementos da matriz B.       #
# Parâmetros de entrada: 15 números reais do vetor A.                          #
# Valores de saída: Vetor B com os valores transformados conforme a paridade   #
#                   do índice.                                                 #
# Autor: Vinicius Gabriel Marcelino Maciel                                     #
################################################################################

vetor_a = []
for indice in range(15):
    valor = float(input(f"A[{indice}]: ").replace(",", "."))
    vetor_a.append(valor)

vetor_b = []
for indice, valor in enumerate(vetor_a):
    if indice % 2 == 0:
        vetor_b.append(valor / 2)
    else:
        vetor_b.append(valor * 1.5)

print("Vetor B:", vetor_b)
