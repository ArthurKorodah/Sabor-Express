import os

restaurantes = [{'nome': 'PizzaPie', 'categoria': 'pizza', 'ativo': False},
                {'nome': 'MolhoDoBom', 'categoria': 'italiano', 'ativo': True},
                {'nome': 'SoulShii', 'categoria': 'japones', 'ativo': False}]

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
    voltar_menu_inicial()

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
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' - {nome_restaurante} | {categoria} | {ativo}\n')
    voltar_menu_inicial()


def opcao_escolhida():
    try:
        opcao_escolhida = int(input('Escolha uma opção:\n'))
        #Modo1 print('Você escolheu a opção ' + opção_escolhida + '.')
        #Modo2 print(f'Você escolheu a opção {opção_escolhida}')
        #opção_escolhida = input('Escolha uma opção:\n')
        #Transformar a var 'str' do input em 'int'
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar Restaurante.\n')
            case 4:
                finalizar_app()
            case _:
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
