#Operações básicas

faturamento = 1000
custo = 700
novas_vendas = 300
taxa_imposto = 0.1
taxa_restituicao = 0.1

faturamento = faturamento + novas_vendas # Soma
imposto = faturamento * taxa_imposto # Multiplicação
lucro = faturamento - custo - imposto # Subtração
margem_lucro = lucro / faturamento # Divisão
restituicao = imposto * taxa_restituicao

print(f"Faturamento: {faturamento}")
print(f"Lucro: {lucro}")
print(f"Margem: {margem_lucro}") 
print(f"Imposto: {imposto}") 
print(f"Restituição: {restituicao}") 