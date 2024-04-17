import os

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

def opcao_escolhida():
    #Modo1 print('Você escolheu a opção ' + opção_escolhida + '.')
    #Modo2 print(f'Você escolheu a opção {opção_escolhida}')
    #opção_escolhida = input('Escolha uma opção:\n')
    opção_escolhida = int(input('Escolha uma opção:\n'))
    #Transformar a var 'str' do input em 'int'

    if opção_escolhida == 1:
        print('Cadastrar Restaurante.')
    elif opção_escolhida == 2:
        print('Listar Restaurantes.')
    elif opção_escolhida == 3:
        print('Ativar Restaurante.')
    elif opção_escolhida == 4:
        finalizar_app()
    else:
        print('Escolha uma das opções listadas acima.') 

def finalizar_app():
    os.system('clear')
    print('Encerrando Programa...')

def main():
    exibir_nome_programa()
    exibir_menu_inicial()
    opcao_escolhida()

if __name__ == '__main__':
    main()
