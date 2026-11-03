def carregar_registros(nome_arquivo):
    registros = []
    ref_arq = open(nome_arquivo, 'a')
    ref_arq.close()
    ref_arq = open(nome_arquivo, 'r')
    for linha in ref_arq:
        linha = linha.strip()
        if linha != "":
            registros.append(linha.split(";"))
    ref_arq.close()
    return registros

def salvar_registros(nome_arquivo, registros):
    ref_arq = open(nome_arquivo , 'w')
    for registro in registros:
        linha = ""
        for i in range(len(registro)):
            if i > 0:
                linha = linha + ";"
            linha = linha + registro[i]
        ref_arq.write(linha + "\n")
    ref_arq.close()

def listasdomenuprincipal():
    print('***********Pesquisa de Opinião publica***********')
    print('1. Pessoa')
    print('2. Pesquisa')
    print('3. Resposta da Pesquisa')
    print('4. Relatórios')
    print('5. Sair')
    op = int(input('Digite de 1 a 4 para escolher sua opção ou digite 5 para sair: '))
    return op

def main():
    pessoas = carregar_registros("pessoas.txt")
    pesquisas = carregar_registros("pesquisas.txt")
    respostas = carregar_registros("respostas.txt")

    opcao = 0
    while opcao != 5:
        opcao = listasdomenuprincipal()
        if opcao == 1:
            submenu_pessoa(pessoas)
            salvar_registros("pessoas.txt" , pessoas)
        elif opcao == 2:
            submenu_pesquisa(pesquisas)
            salvar_registros("pesquisas.txt" , pesquisas)
        elif opcao == 3:
            submenu_resposta(pessoas, pesquisas, respostas)
            salvar_registros("respostas.txt", respostas)
        elif opcao == 4:
            submenu_relatorios(pessoas, pesquisas, respostas)
        elif opcao == 5:
            print("Programa encerrado")
        else:
            print("Opção invalida, escolha outra opção")


#codigo da pessoa

def cpf_existe(pessoas, cpf):
    pos = -1
    for i in range(len(pessoas)):
        if pessoas[i][0] == cpf:
            pos = i
    return pos

def incluir_pessoa(pessoas):
    cpf = input("Digite seu CPF:")
    if cpf_existe(pessoas, cpf) != -1:
        print("CPF já cadastrado")
        return -1
    nome = input("Digite seu nome:")
    nascimento = input("Digite sua data de nascimento:")
    sexo = input("Digite seu sexo:")
    telefones = input("Digite seu número de telefone:")
    escolaridade = input("Digite seu nível de escolaridade:")
    pessoas.append([cpf, nome, nascimento, sexo, telefones, escolaridade])
    pos = len(pessoas) - 1
    print("Pessoa cadastrada!")
    return pos

def listar_todos(pessoas):
    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada.")
        return 0
    for i in range(len(pessoas)):
        print("Posição:", i)
        print("CPF:", pessoas[i][0])
        print("Nome:", pessoas[i][1])
        print("Nascimento:", pessoas[i][2])
        print("Sexo:", pessoas[i][3])
        print("Telefones:", pessoas[i][4])
        print("Escolaridade:", pessoas[i][5])
        print("------")
    return len(pessoas)


def submenu_pessoa(pessoas):
    opcao = 1
    while opcao != 0:
        print("---Submenu Pessoa---")
        print("1. Listar todos")
        print("2. Listar um")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("0. Voltar")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            listar_todos(pessoas)

        elif opcao == 2:
            listar_um(pessoas)

        elif opcao == 3:
            incluir_pessoa(pessoas)

        elif opcao == 4:
            alterar_pessoa(pessoas)

        elif opcao == 5:
            excluir_pessoa(pessoas)

        elif opcao != 0:
            print("Opção inválida")


def listar_um(pessoas):
    cpf = input("Digite o CPF da pessoa:")
    pos = cpf_existe(pessoas, cpf)
    if pos == -1:
        print("Pessoa não encontrada.")
        return -1
    print("Posição:", pos)
    print("CPF:", pessoas[pos][0])
    print("Nome:", pessoas[pos][1])
    print("Nascimento:", pessoas[pos][2])
    print("Sexo:", pessoas[pos][3])
    print("Telefones:", pessoas[pos][4])
    print("Escolaridade:", pessoas[pos][5])
    return pos

def alterar_pessoa(pessoas):
    cpf = input("Digite o CPF da pessoa que deseja alterar: ")
    pos = cpf_existe(pessoas, cpf)
    if pos == -1:
        print("Pessoa não encontrada.")
        return -1
    novo_cpf = input("Novo CPF (enter para manter):")
    if novo_cpf != "" and novo_cpf != cpf:
        if cpf_existe(pessoas, novo_cpf) != -1:
            print("CPF já cadastrado")
            return -1
        pessoas[pos][0] = novo_cpf
    pessoas[pos][1] = input("Novo nome: ")
    pessoas[pos][2] = input("Nova data de nascimento: ")
    pessoas[pos][3] = input("Novo sexo: ")
    pessoas[pos][4] = input("Novo telefone: ")
    pessoas[pos][5] = input("Nova escolaridade: ")
    print("Pessoa alterada")
    return pos

def excluir_pessoa(pessoas):
    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada.")
        return -1
    pos = int(input("Digite a posição da pessoa que deseja excluir: "))
    if pos < 0 or pos >= len(pessoas):
        print("Posição inválida")
        return -1
    print("CPF:", pessoas[pos][0])
    print("Nome:", pessoas[pos][1])
    print("Nascimento:", pessoas[pos][2])
    print("Sexo:", pessoas[pos][3])
    print("Telefones:", pessoas[pos][4])
    print("Escolaridade:", pessoas[pos][5])
    confirmacao = input("Deseja realmente excluir?(sim/não): ")
    if confirmacao == "sim" or confirmacao == "Sim":
        del pessoas[pos]
        print("Pessoa excluida!")
        return pos
    else:
        print("Pessoa não excluida.")
        return -1


#codigo da pesquisa

def submenu_pesquisa(pesquisas):
    opcao = 1
    while opcao != 0:
        print('---Submenu Pesquisa---')
        print('1. Listar todas')
        print('2. Listar um')
        print('3. Incluir')
        print('4. Alterar')
        print('5. Excluir')
        print('0. Voltar')    
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            listar_todas_pesquisas(pesquisas)

        elif opcao == 2:
            listar_umpesquisa(pesquisas)
        elif opcao == 3:
            incluir_pesquisas(pesquisas)

        elif opcao == 4:
            alterar_pesquisa(pesquisas)

        elif opcao == 5:
            excluir_pesquisas(pesquisas)

        elif opcao != 0:
            print('Opção inválida')

    return pesquisas

def pesquisa_existe(pesquisas, codigo):
    pos = -1
    for i in range(len(pesquisas)):
        if pesquisas[i][0] == codigo:
            pos = i
    return pos

def listar_todas_pesquisas(pesquisas):
    if len(pesquisas) == 0:
        print('Nenhuma pesquisa cadastrada')

    for i in range (len(pesquisas)):
        print('Código:', pesquisas[i][0], '| Descrição:', pesquisas[i][1])
    return len(pesquisas)

def listar_umpesquisa(pesquisas):
    codigo = input('Código da pesquisa: ')
    pos = pesquisa_existe(pesquisas, codigo)
    if pos == -1:
        print('Pesquisa não encontrada')
        return -1
    print('Código:', pesquisas[pos][0], '| Descrição:', pesquisas[pos][1])
    return pos

def incluir_pesquisas(pesquisas):
    codigo = input('Digite um novo codigo da pesquisa: ')
    if pesquisa_existe(pesquisas, codigo) != -1:
        print('Já existe uma pesquisa com esse código')
        return -1
    descricao = input('Descrição: ')
    pesquisas.append([codigo, descricao])
    pos = len(pesquisas) - 1
    print('Pesquisa incluída com sucesso')
    return pos

def alterar_pesquisa(pesquisas):
    codigo = input('Digite o codigo da pesquisa que deseja alterar: ')
    pos = pesquisa_existe(pesquisas, codigo)
    if pos == -1:
        print('Pesquisa não encontrada')
        return -1
    print('Descrição atual:', pesquisas[pos][1])
    nova_descricao = input('Nova descrição: ')
    pesquisas[pos][1] = nova_descricao
    print('Pesquisa alterada com sucesso')
    return pos

def excluir_pesquisas(pesquisas):
    codigo = input('Digite o codigo da pesquisa que queira excluir: ')
    pos = pesquisa_existe(pesquisas, codigo)
    if pos == -1:
        print('Pesquisa não encontrada')
        return -1
    print('Código:', pesquisas[pos][0], '| Descrição:', pesquisas[pos][1])
    confirmacao = input('Confirmar a exclusão? (sim/não):')
    if confirmacao == 'sim' or confirmacao == 'SIM' or confirmacao == 'Sim':
        del pesquisas[pos]
        print('Pesquisa excluída com sucesso')
        return pos
    else:
        print('Exclusão cancelada')
        return -1

#codigo da respostas

def submenu_resposta(pessoas,pesquisas, respostas):
    opcao = 1
    while opcao != 0:
        print("---Submenu Resposta da Pesquisa---")
        print("1. Listar todas")
        print("2. Listar uma")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("0. Voltar")
        opcao = int(input("Escolha uma opcao: "))
        if opcao == 1:
            listar_todos_respostas(respostas)
        elif opcao == 2:
            listar_uma_resposta(respostas)
        elif opcao == 3:
            incluir_resposta(pessoas, pesquisas, respostas)
        elif  opcao == 4:
            alterar_resposta(respostas)
        elif opcao == 5:
            excluir_resposta(respostas)
        elif opcao != 0:
            print("Opção inválida")

def resposta_existe(respostas,cpf,codigo,data):
    pos = -1
    for i in range(len(respostas)):
        if respostas[i][0] == cpf and respostas[i][1] == codigo and respostas[i][2] == data:
            pos = i
    return pos

def data_existe(respostas, data):
    pos = -1
    for i in range (len(respostas)):
        if respostas [i][2] == data:
            pos = i
    return pos

def incluir_resposta(pessoas, pesquisas, respostas):
    cpf = input("Digite o CPF da pessoa: ")
    if cpf_existe(pessoas, cpf) == -1:
        print("Pessoa não cadastrada")
        return -1
    codigo = input("Digite o código da pesquisa: ")
    if pesquisa_existe(pesquisas, codigo) == -1:
        print("Pesquisa não cadastrada")
        return -1
    data = input("Digite a data(dd/mm/aaaa):")
    if resposta_existe(respostas, cpf, codigo, data ) != -1:
        print("Resposta já cadastrada")
        return -1
    texto_resposta = input("Digite a resposta:")
    respostas.append([cpf, codigo, data, texto_resposta])
    print("Resposta incluída com sucesso")
    return len(respostas) -1

def listar_todos_respostas(respostas):
    if len(respostas) == 0:
        print("Nenhuma resposta cadastrada.")
        return 0 
    for i in range(len(respostas)):
        print("CPF da pessoa: ", respostas[i][0])
        print("Código da pesquisa: ", respostas[i][1])
        print("Data da pesquisa:", respostas[i][2])
        print("Resposta pesquisa:", respostas[i][3])
        print("---------")
    return len(respostas)

def listar_uma_resposta(respostas):
    cpf = input("Digite o CPF da pesquisa:")
    codigo = input("Digite o código da pesquisa:")
    data = input("Digite a data da (dd/mm/aaaa):")
    pos = resposta_existe(respostas,cpf, codigo,data)
    if pos == -1:
        print("Resposta não encontrada.")
        return -1
    print("CPF da pessoa:", respostas[pos][0])
    print("Código da pesquisa:", respostas[pos][1])
    print("Data da pesquisa:", respostas[pos][2])
    print("Resposta da pesquisa:",respostas[pos][3])
    return pos

def alterar_resposta(respostas):
    cpf = input("Digite o CPF da pessoa: ")
    codigo = input("Digite o código: ")
    data = input("Digite a data(dd/mm/aaaa):")
    pos = resposta_existe(respostas,cpf, codigo,data)
    if pos == -1:
        print("resposta não encontrada.")
        return -1
    print("Resposta atual:", respostas[pos][3])
    respostas[pos][3] = input("Nova resposta:")
    print("Resposta alterada:")
    return pos

def excluir_resposta(respostas):
    cpf = input("Digite o CPF da pessoa:")
    codigo = input("Digite o código da pesquisa:")
    data = input("Digite a data(dd/mm/aaaa):")
    pos = resposta_existe(respostas,cpf,codigo,data)
    if pos == -1:
        print("Resposta não encontrada.")
        return -1
    print("CPF da pessoa:", respostas[pos][0])
    print("Código da pesquisa:", respostas[pos][1])
    print("Data: ", respostas[pos][2])
    print("Resposta:" , respostas[pos][3])
    confirmacao = input("Deseja realmente excluir?(sim/não):")
    if confirmacao == "sim" or confirmacao == "Sim":
        del respostas [pos]
        print("Resposta excluída!")
        return pos
    else:
        print("Resposta não excluída.")
        return -1

#codigo dos relatorios

def data_para_comparar(data):
    partes = data.split('/')
    return partes[2] + partes[1] + partes[0]

def mostrar_e_salvar_relatorio(linhas, nome_arquivo):
    ref_arq = open(nome_arquivo, 'w')
    for linha in linhas:
        print(linha)
        ref_arq.write(linha + '\n')
    ref_arq.close()
    print('Relatório salvo em', nome_arquivo)

def relatorio_telefones(pessoas):
    cpf = input('Digite o CPF da pessoa: ')
    pos = cpf_existe(pessoas,cpf)
    if pos == -1:
        print('Pessoa não encontrada')
        return -1
    linhas = ["Telefones de " + pessoas[pos][1] + ": " + pessoas[pos][4]]
    mostrar_e_salvar_relatorio(linhas, 'relatorio_telefone.txt')
    return pos

def relatorio_respostas_pesquisa(pesquisas, respostas):
    codigo = input('Digite o código da pesquisa: ')
    data = input('Digite a data (dd/mm/aaaa): ')
    if data_existe(respostas, data) == -1:
        print('Nenhuma resposta cadastrada nessa data')
        return -1
    pos = pesquisa_existe(pesquisas, codigo)
    if pos == -1:
        print('Pesquisa não encontrada')
        return -1
    linhas = ['Descrição: ' + pesquisas[pos][1]]
    for i in range (len(respostas)):
        if respostas[i][1] == codigo and respostas[i][2] == data:
            linhas.append('CPF: ' + respostas[i][0] + " - Resposta: " + respostas[i][3])
    if len(linhas) == 1:
        linhas.append('Nenhuma resposta nessa data')
    mostrar_e_salvar_relatorio(linhas, 'relatorio_respostas.txt')
    return pos

def relatorio_pesquisas_entre_datas(pesquisas, respostas):
    dataum = input('Digite a data inicial (dd/mm/aaaa): ')
    datadois = input('Digite a data final (dd/mm/aaaa): ')
    inicio = data_para_comparar(dataum)
    fim = data_para_comparar(datadois)
    codigos_mostrado = []
    linhas = []
    for i in range(len(respostas)):
        data_resposta = data_para_comparar(respostas[i][2])
        if data_resposta >= inicio and data_resposta <= fim:
            codigo = respostas[i][1]
            if codigo not in codigos_mostrado:
                codigos_mostrado.append(codigo)
                pos = pesquisa_existe(pesquisas, codigo)
                if pos != -1:
                    linhas.append('Código: ' + pesquisas[pos][0])
                    linhas.append('Descrição: ' + pesquisas[pos][1])
                    linhas.append('------')
    if len(linhas) == 0:
        linhas.append('Nenhuma pesquisa realizada nesse período')
    mostrar_e_salvar_relatorio(linhas, 'relatorio_periodo.txt')
    return len(codigos_mostrado)

def submenu_relatorios(pessoas, pesquisas, respostas):
    opcao = 1
    while opcao != 0:
        print('---Submenu Relatorios---')
        print('1. Telefones de uma pessoa')
        print('2. Respostas de uma pesquisa em uma data')
        print('3. Pesquisas realizadas entre duas datas')
        print('0. Voltar')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            relatorio_telefones(pessoas)

        elif opcao == 2:
            relatorio_respostas_pesquisa(pesquisas, respostas)

        elif opcao == 3:
            relatorio_pesquisas_entre_datas(pesquisas, respostas)

        elif opcao != 0:
            print('Opção inválida')
main()
