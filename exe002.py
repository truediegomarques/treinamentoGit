produtos = ["iphone","ipad","airpod"]
precos = [1500,1000,800,2000]

novo_produto = input("Digite o novo produto:")
novo_produto = novo_produto.lower()

if novo_produto in produtos:
    posicao = produtos.index(novo_produto)
    preco = precos[posicao]
    print(f"Produto {novo_produto} já cadastrado, preco {preco}.")
else:
    produtos.append(novo_produto)
    print(f"{novo_produto} cadastrado com sucesso.")
    
print(produtos)
