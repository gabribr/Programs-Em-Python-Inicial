import random

cpfs = []  # Lista simples Python — muito mais fácil que numpy para armazenar listas

def exibir_tabela():
    print("9º dígito  Região  Estados")
    print("0 - RS")
    print("1 - DF, GO, MT, MS")
    print("2 - AC, AM, AP, PA, RO, RR")
    print("3 - CE, MA, PI")
    print("4 - AL, PB, PE, RN")
    print("5 - BA, SE")
    print("6 - MG")
    print("7 - ES, RJ")
    print("8 - SP")
    print("9 - PR, SC")
    print("10 - sair")

exibir_tabela()
localidade = int(input("Digite sua localidade de acordo com a tabela acima: "))

while localidade < 10:
    cpf = [0] * 11  # CORREÇÃO 1: cria uma lista nova a cada iteração

    # CORREÇÃO 2: gera os 9 primeiros dígitos diretamente com um for
    for i in range(9):
        cpf[i] = random.randint(0, 9)

    # CORREÇÃO 3: simplificado — o 9º dígito (índice 8) é a própria localidade
    cpf[8] = localidade

    # Cálculo do 1º dígito verificador
    numv1 = sum(cpf[i] * (10 - i) for i in range(9))
    resto1 = numv1 % 11
    cpf[9] = 0 if resto1 < 2 else 11 - resto1

    # Cálculo do 2º dígito verificador
    numv2 = sum(cpf[i] * (11 - i) for i in range(10))
    resto2 = numv2 % 11
    cpf[10] = 0 if resto2 < 2 else 11 - resto2

    # Exibe o CPF formatado
    cpf_str = f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"
    print(f"CPF gerado: {cpf_str}")

    # CORREÇÃO 4: salvar na lista é simples assim
    cpfs.append(cpf[:])  # cpf[:] copia a lista para não guardar referência

    print("\n")
    input("Pressione Enter para continuar...")
    print("\n" * 6)
    exibir_tabela()
    localidade = int(input("Digite sua localidade de acordo com a tabela acima: "))

# Exibe todos os CPFs gerados na sessão
print("\nTodos os CPFs gerados:")
for c in cpfs:
    print(f"{c[0]}{c[1]}{c[2]}.{c[3]}{c[4]}{c[5]}.{c[6]}{c[7]}{c[8]}-{c[9]}{c[10]}")