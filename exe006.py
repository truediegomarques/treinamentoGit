#regra imposto
#preco até 1000 -> imposto é de 10%
#preco maior que 1000 -> imposto é de 15%

lista_precos = [4000,8000,2000,1500,900,8000,550]
imposto_acumulado = 0

print(f"Acumulado: {imposto_acumulado}")

for preco in lista_precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
        
    imposto_acumulado = imposto_acumulado + imposto
    print(f"Preco: {preco}, Imposto: {imposto}")
print(f"Acumulado: {imposto_acumulado}")