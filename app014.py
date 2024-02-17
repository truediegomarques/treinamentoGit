#permite acessar recursos do sistema operacional
# import os

# arquivos = os.listdir("CursoGYTB")
# print(arquivos)

# for nome_arquivo in arquivos:
#     if "txt" in nome_arquivo:
#         if "22" in nome_arquivo:
#             os.rename(f"arquivos/{nome_arquivo}",f"arquivos/22/{nome_arquivo}")
#         elif "23" in nome_arquivo:
#             os.rename(f"arquivos/{nome_arquivo}",f"arquivos/23/{nome_arquivo}")
            

#permite acessar recursos da web            
import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)
dic_resp = resposta.json()
cotacao_dolar = dic_resp["USDBRL"]
print(cotacao_dolar)
print(cotacao_dolar["bid"])