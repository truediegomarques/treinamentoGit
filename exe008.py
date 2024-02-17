#Exercício

vendas = {"Andre": [1000,500,300,5000,1500,80,3000],
          "Andressa": [1500,9000,300,150,1500,120,130,55,500,8500],
          "Alan": [800,100],
          "Ana": [800,900,950,1200,1600,130,50,50,50,50,65,60,70,70,70,200,180]
          }

#vendas.items() retorna uma lista de tuplas

def calcular_comissao(nome, vendas):
    comissao = 0
    
    for com in vendas:
        comissao = comissao + 2 + (com * 0.01)
    return nome, comissao

bonus_total = 0
for vendedor in vendas:
    lista_vendas = vendas[vendedor]
    vendedor, comissao = calcular_comissao(vendedor, lista_vendas)
    #nome, comissao = calcular_comissao(vendedor, lista_vendas)
    bonus_total = bonus_total + comissao
    print(f"O vendedor {vendedor} vai receber {comissao} em comissões")
print(f"Comissao total {bonus_total}")