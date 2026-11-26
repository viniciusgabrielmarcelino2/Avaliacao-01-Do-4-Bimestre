################################################################################
# Descrição: Elaborar um programa que leia duas matrizes A e B de uma dimensão #
#            com 12 elementos. A matriz A deve aceitar apenas a entrada de     #
#            valores divisíveis por 2 ou 3, enquanto a matriz B deve aceitar   #
#            apenas a entrada de valores que não sejam múltiplos de 5. A       #
#            entrada das matrizes deve ser validada pelo programa e não pelo   #
#            usuário. Construir uma matriz C que seja o resultado da junção    #
#            das matrizes A e B, de forma que contenha 24 elementos.           #
#            Apresentar os elementos da matriz C.                              #
# Parâmetros de entrada: 12 inteiros divisíveis por 2 ou 3 para A e 12         #
#                        inteiros não múltiplos de 5 para B.                   #
# Valores de saída: Vetor C com os 24 elementos de A e B, nessa ordem.         #
# Autor: Vinicius Gabriel Marcelino Maciel                                     #
################################################################################

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro.")


vetor_a = []
while len(vetor_a) < 12:
    valor = ler_inteiro(f"A[{len(vetor_a)}] (divisível por 2 ou 3): ")
    if valor % 2 == 0 or valor % 3 == 0:
        vetor_a.append(valor)
    else:
        print("Valor inválido. Digite um múltiplo de 2 ou de 3.")

vetor_b = []
while len(vetor_b) < 12:
    valor = ler_inteiro(f"B[{len(vetor_b)}] (não múltiplo de 5): ")
    if valor % 5 != 0:
        vetor_b.append(valor)
    else:
        print("Valor inválido. Múltiplos de 5 não entram no vetor B.")

vetor_c = vetor_a + vetor_b
print("Vetor C:", vetor_c)
