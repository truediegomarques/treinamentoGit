#trabalhando com arquivo

##forma padrão que nos obriga a abrir e fechar o arquivo
#arquivo = open("vendas.txt", "r")
##fechamento do arquivo
#arquivo.close()


#forma mais segura com With - esta forma já fecha o arquivo automaticamente
with open("/home/diego/wks_vscode/estudo_python/CursoGYTB/vendas.txt","r") as arquivo:
    
    infos = arquivo.readlines()

vendas_totais = 0

for item in infos:
    item = item.replace("\n","")
    item = item.replace(" ","")
    resultado = item.split(",")
    valor = float(resultado[1])
    vendas_totais = vendas_totais + valor
print(vendas_totais)