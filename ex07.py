################################################################################
# Descrição: Elaborar um programa que leia uma matriz A do tipo vetor com 20   #
#            elementos inteiros. Construir uma matriz B do mesmo tipo e        #
#            dimensão da matriz A, sendo cada elemento da matriz B é o         #
#            somatório de 1 até o valor do elemento correspondente armazenado  #
#            na matriz A. Se o valor do elemento da matriz A[1] for 5, o       #
#            elemento correspondente da matriz B[1] deve ser 15, pois o        #
#            somatório do elemento da matriz A é 1+2+3+4+5. Apresentar os      #
#            elementos da matriz B.                                            #
# Parâmetros de entrada: 20 números inteiros do vetor A.                       #
# Valores de saída: Vetor B com a soma de 1 até cada elemento de A.            #
# Autor: Vinicius Gabriel Marcelino Maciel                                     #
################################################################################

vetor_a = []
for indice in range(20):
    vetor_a.append(int(input(f"A[{indice}]: ")))

vetor_b = []
for limite in vetor_a:
    total = 0
    # Quando limite é menor que 1, o intervalo é vazio e a soma é zero.
    for numero in range(1, limite + 1):
        total += numero
    vetor_b.append(total)

print("Vetor B:", vetor_b)
