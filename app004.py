#Operaçoes com texto

faturamento = 1000
custo = 700
lucro = faturamento - custo
margem = lucro / faturamento

print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")
print("Faturamento: "+ str(faturamento) + ", Custo: " + str(custo) + ", Lucro: " + str(lucro))
print("")
#Formatação numérica
#.2f = , - seperador de milhar, . - vai ter casa decimal, 2 - número de casas decimais, f - float
print(f"Faturamento: R${faturamento:,.2f}\n Custo: R${custo:,.2f}\n Lucro: R${lucro:,.2f}")
#.1% = . - vai ter casa decimal, 1 - número de casas decimais, % - percentual
print(f"Margem: {margem:.1%}")

print("")
print("")

email =  "EMAIL_falso@gmail.com"

#Tornar tudo minúsculo
print(email.lower())

#Pesquisar no texto (retorna a posição do elemento ou -1 se não localizar)
posicao = email.find('@')
#imprimir o domínio do e-mail
print(f"Domínio: {email[11:]}")
#imprimir o usuário do e-mail
print(f"Usuário: {email[:11]}")
#tamanho do texto
print(f"Tamanho: {len(email)}")
#replace no texto
email_trocado = email.replace("gmail.com","hotmail.com")
print(f"e-mail trocado: {email_trocado}") 
print("")
print("")

#Ajustes em textos
nome = "joão lira"
print(f"Original: {nome}")
print(f"Primeira letra: {nome.capitalize()}")
print(f"Primeiras letras: {nome.title()}")


