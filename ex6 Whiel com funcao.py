def menu():
    print('Escolha uma opção abaixo:')
    print('a - aceitar')
    print('r - recusar')
    print('s - sair')

# MAIN
menu()
opcao = input('opcão escolhida: ')
while (opcao != 's'):
    if opcao=='a':
        print("ACEITOU")
    elif opcao == 'r':
        print("RECUSOU")
    else:
        print('OPCAO INVALIDA')

    menu()
    opcao = input('opcão escolhida: ')

print('FIM')