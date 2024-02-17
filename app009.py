#dicionários
dic_precos = {"celular":1500,"camera":1000,
              "fone de ouvido":800,"monitor":2000}

#recuperando valor
preco_celular = dic_precos["celular"]
print(preco_celular) 
#atualizando valor
dic_precos["celular"] = 1900
print(dic_precos)
#adicionando item
dic_precos["iphone"] = 8900
print(dic_precos)
#removendo item
dic_precos.pop("celular")
print(dic_precos)
#tamanho
print(f"Tamanho: {len(dic_precos)}")
#pesquisa sempre por chave
print("monitor" in dic_precos)
#chaves do dicionario
print(dic_precos.keys())
#valores do dicionário
print(dic_precos.values())
