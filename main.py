import json

#declarações de variáveis que serão utilizadas no código
acao_do_user = 0
extrato = []
saldo = 0
deposito = 0
saque = 0
controle = ""
i = 0

#tela de boas-vindas
print("#############################################")
print("#####BEM-VINDO(A) AO SISTEMA BANCARIO V1#####")
print("#############################################\n")

#menu de ação
while True:
    print("Oque você deseja fazer?")
    acao_do_user = int(input(" 1-Deposito\n 2-Saque\n 3-Extrato\n 4-Sair\n Escolha a opção conrespondente: "))

    match acao_do_user:
            case 1:
                while True:
                    print("\nOpção de depósito foi selecionada!\n")
                    deposito = input("Digite o valor que deseja depositar!: ")

                    #lógica para que a operação de depositivo ocorra
                    saldo =+ float(deposito)
                    extrato.append("+ R$" + deposito)
                    print("\nO valor foi depositado!\n")

                    # estrutura que controla se o user deseja realizar a operação novamente
                    controle = input("Deseja continuar? [S/N]: ")
                    if controle == "S":
                        continue
                    else:
                        break

            case 2: 
                print("\nOpção de saque foi selecionada!\n")

                #vai repetir 3 vezes poís existe um limite de 3 saques diários
                while i < 3:
                    i = i + 1
                    saque = float(input("Digite o valor que deseja saque!: "))

                    if saque > 500:
                        print("Operação inválida!\nLimite máximo de R$500 por saque.")
                        # zerar o valor do saque para evitar repetições desnecessárias
                        saque = 0

                    elif saque > saldo:
                        print("Operação inválida!\nSaldo não disponível.")
                        #zerar o valor do saque para evitar repetições desnecessárias
                        saque = 0
                        
                    else:
                        saldo = saldo - saque
                        saque = str(saque)
                        extrato.append("- R$" + saque)
                        print("\nO valor foi retirado!\n")

                        #estrutura que controla se o user deseja realizar a operação novamente
                        controle = input("Deseja continuar? [S/N]: ")
                        controle = controle.upper()
                        if controle == "S":
                            continue
                            controle = " "

                        else:
                            break
                            controle = " "
                #mensagem caso o user tente fazer mais de 3 tentativas de saque
                if i == 3:
                    print("\nLimite diario de 3 tentativas ultrapassado.")

            case 3:
                print("\nOpção de extrato foi selecionada!\n")

                #imprime todas as operações realizadas até agora
                for uso_conta in extrato:
                    print(uso_conta)

                #por fim imprime o saldo atual da conta
                print(f"O saldo atual da conta é: R$ {saldo}")

                #exportanto o extrato para um arquivo JSON
                arquivo = open("extrato.json", "w")
                json.dump(extrato, arquivo)
                arquivo.close()

            case 4:
                print("\nObrigado por utilizar nossos serviços! :)\n")
                break

            case default:
                print("\nSelecione uma opção válida!\n")