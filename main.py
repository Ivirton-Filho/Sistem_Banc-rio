#declarações de variáveis que serão utilizadas no código
acao_do_user = 0
extrato = [" "]
deposito = 0


#tela de boas-vindas
print("#############################################")
print("#####BEM-VINDO(A) AO SISTEMA BANCARIO V1#####")
print("#############################################\n")

#menu de ação
while True:
    print("Oque você deseja fazer?")
    acao_do_user = int(input(" 1-Deposito\n 2-Saque\n 3-Extrato\n 4-Sair\n Escolha a opção conrespondente: "))

    if acao_do_user < 1 or acao_do_user >= 5:
        print("\nPorfavor, digite uma alternativa valida.")
    else :
        match acao_do_user:
            case 1:
                print("\nOpção de depósito foi selecionada!\n")
                deposito = "+" + input("Digite o valor que deseja depositar!: ")
                extrato.append(deposito)
                print("\nO valor foi depositado!\n")
            
                
   
