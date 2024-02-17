#1% das vendas
#Recebe um texto
vendas = input("Digite o valor de suas vendas no dia: ")

#Converte texto para float, pode ser feito diretamente no input
vendas = float(vendas)

bonus = vendas * 0.01

print(f"O valor do seu bônus é: R${bonus:,.2f}")