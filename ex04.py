################################################################################
# Descrição: Escrever um programa que possibilite calcular a área total em     #
#            metros de uma residência com os cômodos sala, cozinha, banheiro,  #
#            dois quartos, área de serviço, quintal, garagem, entre outros que #
#            podem ser fornecidos ao programa. O programa deve solicitar a     #
#            entrada do nome, da largura e do comprimento de um determinado    #
#            cômodo. Em seguida, deve apresentar a área do cômodo lido e       #
#            também uma mensagem solicitando ao usuário a confirmação de       #
#            continuar calculando novos cômodos. Caso o usuário responda       #
#            "NÃO", o programa deve apresentar o valor total acumulado da área #
#            residencial.                                                      #
# Parâmetros de entrada: Nome, largura e comprimento em metros de cada cômodo  #
#                        e confirmação para continuar.                         #
# Valores de saída: Área de cada cômodo e área total da residência em metros   #
#                   quadrados.                                                 #
# Autor: Vinicius Gabriel Marcelino Maciel                                     #
################################################################################

def ler_medida(mensagem):
    while True:
        medida = float(input(mensagem).replace(",", "."))
        if medida > 0:
            return medida
        print("A medida deve ser maior que zero.")


area_total = 0.0
while True:
    nome = input("Nome do cômodo: ").strip()
    largura = ler_medida("Largura (m): ")
    comprimento = ler_medida("Comprimento (m): ")
    area = largura * comprimento
    area_total += area
    print(f"Área de {nome}: {area:.2f} m²")

    resposta = input("Calcular outro cômodo? (sim/não): ").strip().lower()
    while resposta not in ("s", "sim", "n", "não", "nao"):
        resposta = input("Responda sim ou não: ").strip().lower()
    if resposta in ("n", "não", "nao"):
        break

print(f"Área total da residência: {area_total:.2f} m²")
