import os

def atividade_alura():
    print('Python na Escola de Programação Alura\n')
    meu_nome = 'Arthur Korodah'
    minha_idade = 23
    print(f'O meu nome é {meu_nome}, e eu tenho {minha_idade} anos.\n')
    print(' A\n L\n U\n R\n A\n')
    #print('A','L','U','R','A',sep='\n')
    #print('''A
    #L
    #U
    #R
    #A''')
    #Aplicação do instrutor ^

    pi = 3.14159
    print(f'O valor de pi é: {pi:.2f}')
atividade_alura()

#def classificar_musica(genero_favorito, genero_musica):
#    if genero_favorito == genero_musica:
#        return 'recomendada'
#    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
#        return 'neutra'
#    else:
#        return 'não recomendada'

#resultado = classificar_musica('Rock', 'Pop')
#print(resultado)


#Exercício 1
print('Escolha um núnero...')
print('Escolhe vai!')
escolha_numero = int(input('Me dá um número, me dá:\n'))
def par_ou_impar():
    if escolha_numero % 2 == 0:
        print('É par!')
    else:
        print('Ímpar aaahhrr!')
par_ou_impar()
#Feito

#Exercício 2
def idade_pessoa():
    idade = int(input('Qual a sua idade? \n'))
    if 0 < idade <= 12:
        print('Você é criançaaa!')
    elif 12 < idade <= 18:
        print('Você é adorrmenscente.')
    elif idade > 18:
        print('Você é adultero... Ops! Adulto.')
    else:
        print('Sinistro...') 
idade_pessoa()
#Feito!

#Exercício 3
nome_usuario = 'batman'
senha_usuario = 'bat2000'
def login():
    nome_digitado = input('Digite o nome de usuário: \n')
    senha_digitada = input('Digite a senha: \n')
    if nome_digitado == nome_usuario and senha_digitada == senha_usuario:
        os.system('clear')
        print('Login Efetuado Com Sucesso!\n')
    else:
        print('O nome de usuário e/ou senha estão incorretos.\n')
login()
#Feito!

#Exercício 4
print('\n')
print('Vamos brincar de nuke bomb! \nMe dê as coordenadas X e Y do local onde iremos brincar!\n')
def jogo_nuke_bomb():
    coordenada_x = float(input('Digite a coordenada X: \n'))
    coordenada_y = float(input('Digite a coordenada Y: \n'))
    print('Certo! Vamos lá!')
    if coordenada_x > 0 and coordenada_y > 0:
        os.system('clear')
        print('Oh! O primeiro quadrante? Pode ser divertido...')
    elif coordenada_x < 0 and coordenada_y > 0:
        os.system('clear')
        print('O segundo quadrante costuma revidar, mas nós daremos conta!')
    elif coordenada_x < 0 and coordenada_y < 0:
        os.system('clear')
        print('KAABUUUM! AAHAHAHA O TERCEIRO SEMPRE É DIVERTIDO!')
    elif coordenada_x > 0 and coordenada_y < 0:
        os.system('clear')
        print('Hmmm... O quarto quadrante tem bastante água em volta, pode ser interessante.')
    else:
        os.system('clear')
        print('Nããão! O eixo é nossa própria localização! AAAAAAAHH!')
jogo_nuke_bomb()
#Feito!
