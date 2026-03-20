def coletar_dados_contato():
    while True:
        nome = input("\nDigite o nome do contato: ")
        if len(nome) <= 50 and nome.replace(" ", "").isalpha():
            nome = nome.title()
            break
        else:
            print("\nNome inválido! Digite apenas letras (máximo 50 caracteres).")
    while True:
        telefone_bruto = input("Digite o numero do contato (11 dígitos com DDD): ")
        if len(telefone_bruto) == 11 and telefone_bruto.isdigit():
            ddd = telefone_bruto[:2]
            primeira_parte = telefone_bruto[2:7]
            segunda_parte = telefone_bruto[7:]
            telefone = f"{ddd} {primeira_parte}-{segunda_parte}"
            break
        else:
            print("\nTelefone inválido! Digite exatamente 11 números, sem espaços ou traços.")
    while True:
        email = input("Digite o email do contato: ")
        if len(email) <= 50 and "@" in email:
            break
        else:
            print("\nEmail inválido! O limite é de 50 caracteres e deve conter o símbolo '@'.")
    return nome, telefone, email

def salvar_contato(agenda, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    agenda.append(contato)
    print(f"\n O contato '{nome}' foi adicionado com sucesso!")

def ver_contatos(agenda):
    if len(agenda) == 0:
        print("\nNão há nenhum contato cadastrado na agenda.")
        return
    print("\nLISTA DE CONTATOS:")
    for indice, contato in enumerate(agenda, start=1):
        favorito = "★" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. ({favorito}) | Nome: {nome} | Telefone: {telefone} | Email: {email}")

def editar_contato(agenda, indice_contato):
    try:
        indice_contato_ajustado = int(indice_contato) - 1
        if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
            print("\nInsira os novos dados para atualizar o contato:")
            novo_nome, novo_telefone, novo_email = coletar_dados_contato()
            agenda[indice_contato_ajustado]["nome"] = novo_nome
            agenda[indice_contato_ajustado]["telefone"] = novo_telefone
            agenda[indice_contato_ajustado]["email"] = novo_email
            print(f"\nO contato '{agenda[indice_contato_ajustado]['nome']}' foi atualizado com sucesso!")
        else:
            print("\nÍndice de contato não encontrado na agenda.")
    except ValueError:
        print("\nErro: Você não digitou um número válido. Tente novamente!")

def deletar_contato(agenda, indice_contato):
    try:
        indice_contato_ajustado = int(indice_contato) - 1
        if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
            contato_excluido = agenda.pop(indice_contato_ajustado)
            print(f"\nO contato '{contato_excluido['nome']}' foi deletado com sucesso!")
        else:
            print("\nÍndice de contato não encontrado na agenda.")
    except ValueError:
        print("\nErro: Você não digitou um número válido. Tente novamente!")

def favoritar_contato(agenda,indice_contato):
    try:
        indice_contato_ajustado = int(indice_contato) - 1
        if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
            if agenda[indice_contato_ajustado]["favorito"] == False:
                agenda[indice_contato_ajustado]["favorito"] = True
                print(f"\nO contato '{agenda[indice_contato_ajustado]['nome']}' foi adicionado aos favoritos com sucesso!")
            else:
                agenda[indice_contato_ajustado]["favorito"] = False
                print(f"\nO contato '{agenda[indice_contato_ajustado]['nome']}' foi removido dos favoritos com sucesso!")
        else:
            print("\nÍndice de contato não encontrado na agenda.")
    except ValueError:
        print("\nErro: Você não digitou um número válido. Tente novamente!")

def ver_contatos_favoritos(agenda):
    favoritos = []
    for contato in agenda:
        if contato["favorito"]:
            favoritos.append(contato)
    if len(favoritos) == 0:
        print("\nNão há nenhum contato salvo como favorito.")
        return
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(favoritos, start=1):
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. (★) | Nome: {nome} | Telefone: {telefone} | Email: {email}")

agenda = []

while True:
    print("""\nMENU GERENCIADOR DA AGENDA:
1. Salvar novo contato
2. Ver contatos
3. Editar contato
4. Deletar contato
5. Marcar/Desmarcar contato como favorito
6. Ver contatos favoritos
7. Sair
""")

    escolha = input("Digite uma opção: ")

    if escolha == "1":
        nome, telefone, email = coletar_dados_contato()
        salvar_contato(agenda, nome, telefone, email)

    elif escolha == "2":
        ver_contatos(agenda)

    elif escolha == "3":
        ver_contatos(agenda)
        if len(agenda) > 0:
            indice_contato = input("\nDigite o número do contato que deseja editar: ")
            editar_contato(agenda, indice_contato)

    elif escolha == "4":
        ver_contatos(agenda)
        if len(agenda) > 0:
            indice_contato = input("\nDigite o número do contato que deseja deletar: ")
            deletar_contato(agenda, indice_contato)

    elif escolha == "5":
        ver_contatos(agenda)
        if len(agenda) > 0:
            indice_contato = input("\nDigite o número do contato que dejesa marcar como favorito: ")
            favoritar_contato(agenda, indice_contato)

    elif escolha == "6":
        ver_contatos_favoritos(agenda)

    elif escolha == "7":
        break

    else:
        print("\nOpção inexistente, tente novamente!")
    
print("\nPrograma encerrado!")
print("\n")
