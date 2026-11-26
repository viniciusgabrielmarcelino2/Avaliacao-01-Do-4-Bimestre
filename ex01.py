################################################################################
# Descrição: Elaborar um programa que apresente os resultados das potências do #
#            valor de base 3, elevado a um expoente que varie do valor 0 até o #
#            valor 15. O programa deve apresentar os valores 1, 3, 9, 27, ...  #
#            14348907. Sugestão: leve em consideração as definições            #
#            matemáticas do cálculo de potência, em que qualquer valor         #
#            numérico diferente de zero elevado a zero é 1, e todo valor       #
#            numérico elevado a 1 é ele próprio. Não use em hipótese nenhuma o #
#            operador aritmético de exponenciação. Resolva o problema com a    #
#            técnica de laço – no braço.                                       #
# Parâmetros de entrada: Nenhum.                                               #
# Valores de saída: As 16 potências de base 3, com expoentes de 0 a 15.        #
# Autor: Vinicius Gabriel Marcelino Maciel                                     #
################################################################################

potencia = 1
for expoente in range(16):
    print(f"3 elevado a {expoente} = {potencia}")
    potencia *= 3
