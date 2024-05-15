def adicionar_alunos(registro_alunos):
    while True:
        nome = input("Digite os nomes dos alunos que deseja registrar: ")
        if nome == "fim":
            break
        registro_alunos[nome] = {}

def remover_aluno(registro_alunos, nome):
    if nome in registro_alunos:
        del registro_alunos[nome]
        print(f"O aluno {nome} foi removido.")
    else:
        print(f"O aluno {nome} não esta registrado no sistema.")

def visualizar_alunos(registro_alunos):
    print("Lista de alunos matriculados:")
    if registro_alunos:
        for nome in registro_alunos.keys():
            print(f"Nome: {nome}")
    else:
        print("Não há alunos matriculados.")

def main():
    registro_alunos = {}

    while True:
        print("Menu:")
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Visualizar Alunos")
        print("4. Sair")

        escolha = input("Escolha uma das opções: ")

        if escolha == "1":
            adicionar_alunos(registro_alunos)
        elif escolha == "2":
            nome = input("Digite o nome do aluno que deseja remover: ")
            remover_aluno(registro_alunos, nome)
        elif escolha == "3":
            visualizar_alunos(registro_alunos)
        elif escolha == "4":
            print("Encerrando. Tenha um bom dia.")
            break
        else:
            print("Opção inválida, escolha uma opção válida.")
main()