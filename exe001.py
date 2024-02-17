#exercícios

nome = "José Diego Marques Ramos"
email = "email_falso@gmail.com"

#descubra o servidor do e-mail

posicao_arroba = email.find("@")
servidor_email = email[posicao_arroba:]

print(f"o servidor do e-mail é: {servidor_email}")

#pegar o primeiro nome do usuário
#construa uma mensagem: usuário "primeiro nome"  cadstrado com sucesso

posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
print(f"Usuário {primeiro_nome} cadastrado com sucesso com {email}")

#construa uma mensagem: Enviamos um link de confirmação para o e-mail j***@gmail.com

texto_modificar = email[1:posicao_arroba]
email_seguro = email.replace(texto_modificar,"***" )
print(f"Enviamos um link de confirmação para o e-mail {email_seguro}")
