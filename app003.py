#Operações especiais
#Mod, resto de divisão inteira

tempo_meses = 160
tempo_anos = int(tempo_meses / 12)
meses_saldo = tempo_meses % 12

print(f"Anos: {tempo_anos} e {meses_saldo} meses") 

#Arredondamento
fator = 11
sem_ajuste = tempo_meses / fator
arredondado = round(tempo_meses / fator)
truncado = int(tempo_meses / fator)
edicao_visual = 139_018_182

print("")
print("")
print(f"Resultado da divisão, sem ajuste: {sem_ajuste}")
print(f"Resultado da divisão, arredondado: {arredondado}")
print(f"Resultado da divisão, truncado: {truncado}")
print(f"Formatação visual: {edicao_visual}")
