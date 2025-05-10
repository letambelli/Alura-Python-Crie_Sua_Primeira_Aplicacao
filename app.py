import os

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

def escolher_opcao():
      opcao_escolhida = int(input('Escolha uma opção: '))

      match opcao_escolhida:
           
            case 1:
                  print('Cadastrar Restaurante')
            case 2:
                  print('Listar Restaurantes')
            case 3:
                  print('Ativar Restaurante')
            case 4:
                  finalizar_app()
                  print('Finalizando app\n')
            case _:
                  print('ERRO')

def main():
    exibir_o_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()