################################################################################
# Descrição: Elaborar um programa que leia 20 elementos (valores reais) para   #
#            temperaturas em graus Celsius e armazene esses valores em uma     #
#            matriz A de uma dimensão. O programa ao final deve apresentar a   #
#            menor, a maior e a média das temperaturas lidas.                  #
# Parâmetros de entrada: 20 temperaturas reais em graus Celsius.               #
# Valores de saída: Menor temperatura, maior temperatura e média em graus      #
#                   Celsius.                                                   #
# Autor: Vinicius Gabriel Marcelino Maciel                                     #
################################################################################

temperaturas = []
for numero in range(1, 21):
    temperatura = float(input(f"Temperatura {numero} (°C): ").replace(",", "."))
    temperaturas.append(temperatura)

print(f"Menor temperatura: {min(temperaturas):g} °C")
print(f"Maior temperatura: {max(temperaturas):g} °C")
print(f"Média: {sum(temperaturas) / len(temperaturas):g} °C")
