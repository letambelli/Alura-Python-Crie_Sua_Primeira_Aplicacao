import os

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

print('1. Cadastrar Restaurante')
print('2. Listar Restaurantes')
print('3. Ativar Restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))

def finalizar_app():
    os.system('cls')

print(f'Você escolheu a opção {opcao_escolhida}')

if opcao_escolhida == 1:
    print('Cadastrar Restaurante')
elif opcao_escolhida == 2:
    print('Listar Restaurantes')
elif opcao_escolhida == 3:
    print('Ativar Restaurante')
elif opcao_escolhida == 4:
    finalizar_app()
    print('Finalizando app\n')
else:
    print('ERRO')