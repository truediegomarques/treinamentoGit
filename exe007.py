#regra imposto
#variacao % de cada mês de 2022 para 2023

vendas_22 = {"jan":15000,"fev":15500,"mar":14000,"abr":16600,"mai":16300,"jun":17000,}
vendas_23 = {"jan":17000,"fev":15000,"mar":17500,"abr":16900,"mai":16000,"jun":18500,}


#saber quanto variou percentualmente cada mes de 2023 em comparacao com 2022

for mes in vendas_22:
    valor_22 = vendas_22[mes]    
    valor_23 = vendas_23[mes]  
    var_percentual = (valor_23 / valor_22) - 1
    print(f"Variacao percentual de {mes}: {var_percentual:.1%}")


#simulem: se a empresa tivesse pelo menos empatado com 2023 nos meses que ela vendeu menos,
#qual teria sido o faturamento

faturamento_simulado = 0

for mes in vendas_22:
    valor_22 = vendas_22[mes]    
    valor_23 = vendas_23[mes]  
    var_percentual = (valor_23 / valor_22) - 1
    if valor_22 > valor_23:
        faturamento_simulado = faturamento_simulado + valor_22    
    else:
        faturamento_simulado = faturamento_simulado + valor_23    
print(f"Simulado: {faturamento_simulado}")