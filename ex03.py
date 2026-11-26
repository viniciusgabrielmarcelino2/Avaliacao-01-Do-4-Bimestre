################################################################################
# Descrição: Elaborar um programa que leia sucessivamente valores numéricos e  #
#            apresente no final o somatório, a média e o total de valores      #
#            lidos. O programa deve ler os valores enquanto o usuário estiver  #
#            fornecendo valores positivos. Ou seja, o programa deve parar      #
#            quando o usuário fornece um valor negativo (menor que zero).      #
# Parâmetros de entrada: Números reais em sequência. Um valor negativo encerra #
#                        a leitura.                                            #
# Valores de saída: Soma, média e quantidade de valores aceitos.               #
# Autor: Vinicius Gabriel Marcelino Maciel                                     #
################################################################################

soma = 0.0
quantidade = 0

while True:
    valor = float(input("Digite um valor (negativo para encerrar): ").replace(",", "."))
    if valor < 0:
        break
    soma += valor
    quantidade += 1

print(f"Soma: {soma:g}")
print(f"Quantidade: {quantidade}")
if quantidade > 0:
    print(f"Média: {soma / quantidade:g}")
else:
    print("Média indefinida, pois nenhum valor foi informado.")
