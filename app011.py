#Definindo funções
#modelo
# def se_inscrever():
#     print("Se inscreve no canal")
    
# se_inscrever()

lista_precos = [4000,8000,2000,1500,900,8000,550]
imposto_acumulado = 0

def calcular_imposto(preco, aliquota1 = 0.2,aliquota2 = 0.15,aliquota3 = 0.1):
    if preco > 2000:
        imposto = preco * aliquota1
    elif preco > 1000:
        imposto = preco * aliquota2
    else:
        imposto = preco * aliquota3
    return imposto

for preco in lista_precos:
    #imposto = calcular_imposto(preco,0.25,aliquota2 = 0.19)
    imposto = calcular_imposto(preco)
    imposto_acumulado = imposto_acumulado + imposto
    print(f"Preco: {preco}, Imposto: {imposto}")
    
print(f"Acumulado: {imposto_acumulado}")

#retornando diversos valores, retorna uma tupla e ela é imutável
def calcular_imposto2(preco, ir = 0.275,csll = 0.035,iss = 0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir,imposto_csll, imposto_iss

resposta = calcular_imposto2(1000)
print(resposta)
# print(resposta[0])
# print(resposta[1])
# print(resposta[2])

#unpacking da tupla
ir, csll, iss = resposta
#com separador
print(ir, csll, iss, sep="\n")