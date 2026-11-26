################################################################################
# Descrição: Escrever um programa que calcule e apresente o somatório do       #
#            número de grãos de trigo que se pode obter num tabuleiro de       #
#            xadrez, obedecendo à seguinte regra: colocar um grão de trigo no  #
#            primeiro quadro e nos quadros seguintes o dobro do quadro         #
#            anterior. Ou seja, no primeiro quadro coloca-se um grão, no       #
#            segundo quadro colocam-se dois grãos (neste momento têm se três   #
#            grãos), no terceiro quadro colocam-se quatro grãos (tendo neste   #
#            momento sete grãos), no quarto quadro colocam-se oito grãos       #
#            (tendo-se então 15 grãos) até atingir o sexagésimo quarto quadro  #
#            (este exercício foi baseado numa situação exposta no capítulo 16  #
#            do livro "0 Homem que Calculava" de Malba Tahan, da Editora       #
#            Record).                                                          #
# Parâmetros de entrada: Nenhum.                                               #
# Valores de saída: Total de grãos acumulados nas 64 casas.                    #
# Autor: Vinicius Gabriel Marcelino Maciel                                     #
################################################################################

graos_na_casa = 1
total = 0

for casa in range(1, 65):
    total += graos_na_casa
    graos_na_casa *= 2

print(f"Total de grãos nas 64 casas: {total}")
