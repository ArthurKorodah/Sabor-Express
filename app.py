import os

restaurantes = ['PizzaPie','MolhoDoBom']

def exibir_nome_programa():
    print('''
        
    ╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
    ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
    ┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
    ╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
    ┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
    ╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
        ''')

def exibir_menu_inicial():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção inválida! Escolha uma das opções listadas acima.')
    input('Aperte ENTER para voltar ao menu inicial.')
    main()

def voltar_menu_inicial():
    input('\nAperte [ENTER] para voltar ao menu inicial.')
    main()

def cadastrar_novo_restaurante():
    os.system('clear')
    print('Cadastro De Restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print('Cadastrando restaurante...\n')
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_inicial()

def listar_restaurantes():
    os.system('clear')
    print('Listando Restaurantes.\n')
    for nome_restaurante in restaurantes:
        print(f'- {nome_restaurante}')
    voltar_menu_inicial()

def opcao_escolhida():
    try:
        #Modo1 print('Você escolheu a opção ' + opção_escolhida + '.')
        #Modo2 print(f'Você escolheu a opção {opção_escolhida}')
        #opção_escolhida = input('Escolha uma opção:\n')
        opção_escolhida = int(input('Escolha uma opção:\n'))
        #Transformar a var 'str' do input em 'int'

        if opção_escolhida == 1:
            print('Cadastrar Restaurante.')
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurantes()
        elif opção_escolhida == 3:
            print('Ativar Restaurante.')
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    os.system('clear')
    print('Encerrando Programa...')

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_menu_inicial()
    opcao_escolhida()

if __name__ == '__main__':
    main()
