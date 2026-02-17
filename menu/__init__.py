import os

BASE_DIR = 'arquivos'

def menu():
  print('-'*30)
  print('\tMENU PRINCIPAL')
  print('-'*30)
  print('0 - Criar um arquivo')
  print('1 - Ver pessoas cadastradas')
  print('2 - Cadastrar nova pessoa')
  print('3 - Remover pessoa')
  print('4 - Apagar Arquivo')
  print('5 - Sair do sistema')

  print('-'*30)

def ler_opção(msg):
  while True:
    try:
      option = int(input(msg))
    except ValueError:
      print(f'\033[0;31mErro valor inválido! \033[m')
      continue
    else:
      return option
    
def criar_arquivo():
  nome_arquivo= input('Nome do arquivo a ser criado?').strip()
  caminho = os.path.join(BASE_DIR, f"{nome_arquivo}.txt")
  with open(caminho,'a'):
     pass

  print('-'*40)
  print('\t ARQUIVO CRIADO COM SUCESSO')
  print('-'*40)

def listar_pessoas():
  print('-'*40)
  nome_arquivo = input('Qual arquivo deseja abrir? ').strip()
  caminho = os.path.join(BASE_DIR, f"{nome_arquivo}.txt")

  print('-'*40)
  print(f'\t Lista de Pessoas\t')
  print('-'*40,end='\n')
  
  try:
    with open(caminho, 'r') as f:
        print(f.read())
  except FileNotFoundError:
        print("Arquivo não encontrado.")

def cadastrar_pessoa():
  print('-'*40)
  print('\t Cadastro ')
  print('-'*40)

  try:
    id = int(input('ID: '))
    idade = int(input('Idade: '))
  except ValueError:
    print("ID ou idade inválidos.")
    return

  nome = input('Nome: ').strip()
  nome_arquivo = input('Qual o arquivo desejado? ').strip()

  caminho = os.path.join(BASE_DIR, f"{nome_arquivo}.txt")

  try:
    with open(caminho, 'a') as f:
      f.write(f'\tID: {id}\t NOME: {nome}\t IDADE: {idade} anos\n')
      print(f'{nome} cadastrado(a) com sucesso!')
  except FileNotFoundError:
      print("Arquivo não encontrado.")
      
def remover_pessoa():
  print('-'*40)
  print('\t Remoção ')
  print('-'*40)

  nome_arquivo = input('Qual o arquivo desejado? ').strip()
  caminho = os.path.join(BASE_DIR, f"{nome_arquivo}.txt")


  try:
      id_pessoa = int(input('Qual o ID de quem deseja remover? '))
  except ValueError:
      print("ID inválido.")
      return

  try:
      with open(caminho, 'r') as f:
        linhas = f.readlines()

      with open(caminho, 'w') as f:
        removido = False
        for linha in linhas:
            if f"ID: {id_pessoa}" not in linha:
                f.write(linha)
            else:
                removido = True

      if removido:
          print(f'Pessoa com ID {id_pessoa} removida com sucesso.')
      else:
          print('Pessoa não encontrada.')

  except FileNotFoundError:
      print('Arquivo não encontrado.')



def remover_arquivo():
  nome_arquivo = input('Qual o nome do arquivo a ser removido? ').strip()
  caminho = os.path.join(BASE_DIR, f"{nome_arquivo}.txt")

  try:
      os.remove(caminho)

      print('-'*40)
      print('\t ARQUIVO APAGADO COM SUCESSO')
      print('-'*40)
  except FileNotFoundError:
      print("Arquivo não encontrado.")


def sistema():
  if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
    
  while True:
    menu()
    option = ler_opção('Sua opção: ')
    if option == 0:
      criar_arquivo()

    elif option == 1:
      listar_pessoas()

    elif option == 2:
      cadastrar_pessoa() 

    elif option ==3:
       remover_pessoa()

    elif option ==4:
      remover_arquivo()

    elif option == 5:
      print('-'*40)
      print('\t SAINDO DO SISTEMA....Até logo')
      print('-'*40)
      break
    else: 
      print(f'\033[0;31mErro "{option}" não presente nas escolhas\033[m')
      
