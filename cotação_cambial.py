
DOLAR = 5.50 
def trancos( ):
# imprime uma linha de traços para separar seções do console 

     print('-' * 50)


def converter_para_dolar(valor_em_reais):
#coverte um valor em reais para dólares.:param valor_em_reais: valor em reais a ser  covertido. :return : valor convertido em dólares 
    return valor_em_reais / DOLAR

def converter_para_reias(valor_em_dolares):
# converte um valor  em dólares para reais. :param valor_em_dolar: valor em dólares a ser convertido.
#:return: valor convertido em  reais.
 return valor_em_dolares * DOLAR

print("conversor de moeda | escolha uma opção:")
opcao = int(input("1. converter reais  para Dólares \n2. converter Dólares para Reais :"))
trancos() 

match opcao:
    case 1:
      print("converter Reais para Dólares")
      trancos()
      valor_em_reais = float(input("digite  o valor  em reais:"))
      trancos()
      valor_em_dólares = converter_para_dolar(valor_em_reais) 
      trancos()
      print(f"valor em dólares: {valor_em_dólares:.2f}")
    case 2:
       valor_em_dólares =float(input("Digite o valor em dólares:"))
       trancos()
       valor_em_reais = converter_para_reias(valor_em_dólares)
       trancos()
       print(f"valor em reais : {valor_em_reais:.2f}")
    case _:
       print("Opção inválida. tenta novamente.")
       trancos() 



