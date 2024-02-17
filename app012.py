#estrutura de repetição - while

produtos = []
while True:
    novo_produto = input("Digite o nome do produto:")
    novo_produto = novo_produto.lower()
    
    if "sair" == novo_produto:
        break
    
    if novo_produto in produtos:
        print("Produto já cadastrado")
    else:
        produtos.append(novo_produto)
        print(f"Produto {novo_produto} cadastrado com sucesso")

print(produtos)