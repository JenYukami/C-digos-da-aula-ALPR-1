def carregar_registros(nome_arquivo):
    registros = []
    ref_arq = open(nome_arquivo ,'r')
    for linha in ref_arq:
        registro = linha.strip().split(";")
        registros.append(registro)
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
            print("Opção invalida, escolha outra opção")
        elif opcao == 4:
            print("Opção invalida, escolha outra opção")
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

def pesquisa_existe(pesquisas, codigo):
    for i in range(len(pesquisas)):
        if pesquisas[i][0] == codigo:
            return i
    return -1

def listar_todas_pequisas(pesquisas):
    if len(pesquisas) == 0:
        print('Nenhuma pesquisa cadastrada')
    else:
        for pesquisa in pesquisas:
            print('Código:', pesquisa[0], '| Descrição:', pesquisa[1])

def listar_umpesquisa(pesquisas):
    codigo = int(input('Código da pesquisa: '))
    posicao = pesquisa_existe(pesquisas, codigo)
    if posicao == -1:
        print('Pesquisa não encontrada')
    else:
        print('Código:', pesquisas[posicao][0], '| Descrição:', pesquisas[posicao][1])

def incluir_pesquisas(pesquisas):
    codigo = int(input('Digite um novo codigo da pesquisa: '))
    if pesquisa_existe(pesquisas, codigo) != -1:
        print('Já existe uma pesquisa com esse código')
    else:
        descricao = input('Descrição: ')
        pesquisas.append([codigo, descricao])
        print('Pesquisa incluída com sucesso')

def alterar_pesquisa(pesquisas):
    codigo = int(input('Digite o codigo da pesquisa que deseja alterar: '))
    posicao = pesquisa_existe(pesquisas, codigo)
    if posicao == -1:
        print('Pesquisa não encontrada')
    else:
        print('Descrição atual:', pesquisas[posicao][1])
        nova_descricao = input('Nova descrição: ')
        pesquisas[posicao][1] = nova_descricao
        print('Pesquisa alterada com sucesso')

def excluir_pesquisas(pesquisas):
    codigo = int(input('Digite o codigo da pesquisa que queira excluir: '))
    posicao = pesquisa_existe(pesquisas, codigo)
    if posicao == -1:
        print('Pesquisa não encontrada')
        return pesquisas
    print('Código:', pesquisas[posicao][0], '| Descrição:', pesquisas[posicao][1])
    confirmacao = input('Confirmar a exclusão? (sim/não):')
    if confirmacao == 'sim' or confirmacao == 'SIM' or confirmacao == 'Sim':
        del pesquisas[posicao]
        print('Pesquisa excluída com sucesso')
    else:
        print('Exclusão cancelada')

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
            listar_todas_pequisas(pesquisas)

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

def submenu_resposta(pessoas,pesquisas):
    opcao = 1

