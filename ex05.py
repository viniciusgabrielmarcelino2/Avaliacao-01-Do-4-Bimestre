################################################################################
# Descrição: Elaborar um programa que apresente resultado inteiro da divisão   #
#            de dois números quaisquer representando o dividendo e o divisor   #
#            da divisão a ser processada. Sugestão: para a elaboração do       #
#            programa, não utilize o operador aritmético de divisão com        #
#            quociente inteiro. Use uma solução baseada em laço de repetição.  #
#            O programa deve apresentar como resultado (quociente) quantas     #
#            vezes o divisor cabe no dividendo.                                #
# Parâmetros de entrada: Dividendo e divisor, que pode ser positivo ou         #
#                        negativo e deve ser diferente de zero.                #
# Valores de saída: Quociente inteiro, desprezando a parte fracionária.        #
# Autor: Vinicius Gabriel Marcelino Maciel                                     #
################################################################################

from fractions import Fraction

# A fração exata permite subtrair também valores como 0,1 sem erro de arredondamento.
dividendo = Fraction(input("Dividendo: ").strip().replace(",", "."))
divisor = Fraction(input("Divisor: ").strip().replace(",", "."))

if divisor == 0:
    print("Não é possível dividir por zero.")
else:
    restante = abs(dividendo)
    passo = abs(divisor)
    quociente = 0
    while restante >= passo:
        restante -= passo
        quociente += 1

    if (dividendo < 0) != (divisor < 0):
        quociente = -quociente
    print(f"Quociente inteiro: {quociente}")
