#Usando dicionarios
dic_precos = {"celular":1500,"camera":1000,
              "fone de ouvido":800,"monitor":2000}

produto = input("Digite o novo produto:")
produto = produto.lower()

if produto in dic_precos:
    preco = dic_precos[produto]
    print(f"Produto {produto}, preco {preco}.")
else:
    print(f"{produto} não encontrado.")
    
