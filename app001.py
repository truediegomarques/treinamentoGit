# pandas
#from sys import displayhook
import pandas as pd

tabela = pd.read_excel("/home/diego/wks_vscode/estudo_python/PythonExcel/Produtos.xlsx")

df = pd.DataFrame(tabela)

tam = len(df.index)
ind = 0
valor_acumulado = 0 

while ind < tam:
    
    linha = df.loc[ind]
    descricao = linha['produtos']
    preco = linha['preco']
    tipo = linha['tipo']
    imposto = linha['imposto']
    final = preco * imposto
    ind = ind + 1
    print(f"Produto {descricao} preco final {final:,.2f}")
    
    