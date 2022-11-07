#r: somente leitura
#w: escrita, pode alterar o conteúdo do arquivo
#a: adicionar algo a arquivo já existente
#+: leitura e escrita
arquivo = open('cadastro.dat','w')
arquivo.write('Linha 1\n')
arquivo.write('Linha 2\n')
arquivo.close()

arquivo = open('cadastro.dat','r')
for linha in arquivo:
    print(linha)
arquivo.close()

#1 - tenha o arquivo criado (mesmo que vazio)
#2 - Faça uma carga completo no início do programa do Meio Secundário para  a Memória Principal
#  - Evite trabalhar com o arquivo aberto.
#3 - Ao sair do programa descarregue o conteúdo da memória principal para a memória secundária

pessoas = []
# Realizando a carga do arquivo em uma lista de pessoas
with open('pessoas.dat','r') as arquivo:
    for linha in arquivo:
        campos = linha.split(',')
        pessoa = {}
        pessoa['nome'] = campos[0]
        pessoa['email'] = campos[1]
        pessoa['telefone'] = campos[2]
        pessoas.append(pessoa)

print(pessoas[1]['nome']) #Busca o nome da segunda pessoa

# trabalhar com os dados na lista

# atualizou o email da segunda pessoa
#pessoas[1]['email'] = 'josefina@algo.com.br'

# Cadastrou uma nova pessoa
#pessoa = {}
#pessoa['nome'] = 'Carla'
#pessoa['email'] = 'Carla@gmail.com'
#pessoa['telefone'] = '(65) 132'
#pessoas.append(pessoa)

# Ao sair salvar todas as pessoas no arquivo
with open('pessoas.dat','w') as arquivo:
    for pessoa in pessoas:
        pessoa_str = f"{pessoa['nome']},{pessoa['email']},{pessoa['telefone']}"
        arquivo.write(pessoa_str)


