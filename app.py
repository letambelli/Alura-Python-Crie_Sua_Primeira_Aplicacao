import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': False}, 
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]


def exibir_o_nome_do_programa():
      '''Essa função exibe o nome estilizado do programa na tela.'''

      print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
      """)

def exibir_opcoes():
      '''Exibe as opções disponíveis no menu principal.'''
      print('1. Cadastrar Restaurante')
      print('2. Listar Restaurantes')
      print('3. Alternar Estado do Restaurante')
      print('4. Sair\n')

def finalizar_app():
    '''Exibe a mensagem de finalização do app.'''
    os.system('cls')

def voltar_ao_menu_principal():
      '''Solicita uma tecla para voltar ao menu principal.
      
      Outputs:

      - Retorna ao menu principal
      '''
      input('Aperte uma tecla para voltar ao menu principal.')
      main()

def opcao_invalida():
      '''Exibe uma mensagem de opção inválida e retorna ao menu principal.
      
      Output:

      - Retorna ao menu principal
      '''

      print('Opção inválida!\n')
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):
      '''Exibe um subtítulo estilizado na tela.
      Inputs: 
      
      - Texto: str - O texto do subtítulo
      '''
      os.system('cls')
      linha = '*' * (len(texto) + 4)
      print(linha)
      print(texto)
      print(linha)
      print()

def cadatrar_novo_restaurante():
      '''Essa função é responsável por cadastrar um novo restaurante
      
      Inputs:

      - Nome do Restaurate
      - Categoria

      Outputs:

      - Mensagem de sucessso ao cadastrar o restaurante
      
      '''
      exibir_subtitulo('Cadastro de novos restaurantes')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
      voltar_ao_menu_principal()

def listar_restaurantes():
      '''Lista os restaurantes existentes no dicionário.
      
      Outputs:

      - Nome do restaurante
      - Categoria do restaurante
      - Estatus do restaurante (ativo/desativado)

      '''

      exibir_subtitulo('Listando Restaurantes')
      print(f'{'Nome do Restaurante'.ljust(21)} | {'Categoria'.ljust(20)} |{'Status'}')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
      voltar_ao_menu_principal()

def alternar_estado_restaurante():
      '''Pesquisa um restaurante pelo nome e, caso encontre, altera seu status (ativo/desativado). Caso não haja um restaurante com o nome pesquisado é exibida uma mensagem avisando o usuário que o restaurante não foi encontrado.
      

      Input:

      - Nome do restaurante

      Output:

      - Nome do restaurante
      - Status do restaurante alterado

      ou

      - Mensagem de restaurante não encontrado
      
      '''
      exibir_subtitulo('Alternando o estado do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
      restaurante_encontrado = False

      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
                  print(mensagem)
      if not restaurante_encontrado:
            print('O restaurante não foi encontrado')



      voltar_ao_menu_principal()

def escolher_opcao():
      '''Permite ao usuário acessar as páginas do programa ao escolhê-las pelo número indicado na lista.
      

      Input:

      - Número da opção

      Output: 

      - Página selecionada

      '''

      try:
            opcao_escolhida = int(input('Escolha uma opção: '))

            match opcao_escolhida:
            
                  case 1:
                        cadatrar_novo_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        alternar_estado_restaurante()
                  case 4:
                        finalizar_app()
                  case _:
                        opcao_invalida()
      except:
            opcao_invalida()

def main():
    '''Inicia a função principal do sistema.'''

    os.system('cls')
    exibir_o_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()