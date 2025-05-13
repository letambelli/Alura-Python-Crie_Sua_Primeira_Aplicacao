import os

restaurantes = ['Pizza', 'Sushi']

def exibir_o_nome_do_programa():
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
      print('1. Cadastrar Restaurante')
      print('2. Listar Restaurantes')
      print('3. Ativar Restaurante')
      print('4. Sair\n')

def finalizar_app():
    os.system('cls')

def opcao_invalida():
      print('Opção inválida!\n')
      input('Aperte uma tecla para voltar ao menu principal.')
      main()

def cadatrar_novo_restaurante():
      os.system('cls')
      print('Cadastro de novos restaurantes\n')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      restaurantes.append(nome_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      input('\nDigite uma tecla para voltar ao menu principal')
      main()

def listar_restaurantes():
      os.system('cls')
      print('Listando Restaurantesz\n')
      for restaurante in restaurantes:
            print(f'{restaurante}')
      input('\nDigite uma tecla para voltar ao menu principal')
      main()

def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))

            match opcao_escolhida:
            
                  case 1:
                        cadatrar_novo_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        print('Ativar Restaurante')
                  case 4:
                        finalizar_app()
                        print('Finalizando app\n')
                  case _:
                        opcao_invalida()
      except:
            opcao_invalida()

def main():
    os.system('cls')
    exibir_o_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()