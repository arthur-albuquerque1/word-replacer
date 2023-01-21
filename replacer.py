def replacer():
    exit = False
    while not exit:
        print('Seja bem vindo ao nosso substituidor de palavras')
        print('1. Iniciar')
        print('2. Sair')

        choice = int(input('Escolha uma das opções: '))

        if choice == 1:
            phrase = input('Digite a frase: ')
            wordinicial = input('Digite a palavra a ser substituída: ')
            wordfinal = input('Digite a palavra substituta: ')
            print(phrase.replace(wordinicial, wordfinal))

        elif choice == 2:
            print('Até a próxima!')
            exit = True
        else:
            print('Opção inválida, tente novamente')


replacer()
