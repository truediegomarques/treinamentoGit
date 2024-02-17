#Trabalhando com listas
vendas = [100,50,130,80,120,250]
produtos = ["iPhone","iPad","airPod"]
precos = [4000,8000,2000]

#tamanho da lista
tam = len(vendas)
#valor máximo da lista
valor_max = max(vendas)
#valor mínimo da lista
valor_min = min(vendas)
#localizando posição de item
posicao = vendas.index(130)
#totalizando vendas
valor_total = sum(vendas)


#retornando valor em posição passada por índice, inicia em 0
print(f"Primeira posição da lista {vendas[0]}") 
#retornando último item da lista
print(f"Última posição da lista {vendas[-1]}") 
#retornando tamanho da lista
print(f"Tamanho da lista {tam}")
#retornando valor máximo da lista
print(f"Valor máximo da lista {valor_max}")
#retornando valor mínimo da lista
print(f"Valor mínimo da lista {valor_min}")
#posição de 130 na lista
print(f"Posição da lista {posicao}")
#imprimir a partir da posição 2, inclui a 2
print(vendas[2:]) 
#imprimir até da posição 2, não inclui a 2
print(vendas[:2]) 
#total das vendas
print(f"Valor total das vendas {valor_total}")
#verificando se produto digitado está na lista
produto_usuario = input("Digite o nome do produto:")
print(produto_usuario in produtos)
#atualizado valor na lista em 10%
precos[0] = precos[0] * 1.1
print(f"Posição da lista {precos[0]}")
#adicionar e imprimir itens nas listas
produtos.append("macBook")
precos.append("10000")
print(produtos)
print(precos)
produtos.remove("macBook")
precos.pop(-1)
print(produtos)
print(precos)
#adicionar item em posicao específica
produtos.insert(1,"airPod")
print(produtos)
print(precos)
#Contar valores
print(produtos.count("airPod"))
#ordenacao direta e invertida
precos.sort()
print(precos)
precos.sort(reverse=True)
print(precos)
