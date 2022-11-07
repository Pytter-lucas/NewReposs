import random
'''
Lista de Exercícios referentes a coleções em python
'''

    #1. Faça um programa que armazene 15 números inteiros em uma lista e depois
    #permita que o usuário digite um número inteiro para ser buscado na lista, se
    #for encontrado o programa deve imprimir a posição desse número na lista, caso
    #contrário, deve imprimir a mensagem: "Nao encontrado!".
lista = []
for cont in range(15):
    lista.append(random.randrange(1,50))
print(lista)
numero = int(input('Informe um número a ser buscado'))
try:
    posicao_encontrada = lista.index(numero)
except:
    posicao_encontrada = -1
if posicao_encontrada >= 0:
    print(f'Encontrado {numero} na posição {posicao_encontrada}')
else:
    print(f'{numero} não encontrado')

    #ALTERNATIVA DE SOLUCAO SEM INDEX
    lista = []
    for cont in range(15):
        lista.append(random.randrange(1,50))
    print(lista)
    numero = int(input('Informe um número a ser buscado'))
    contador = 0
    posicao_encontrada = -1
    for valor_posicao in lista:
        if valor_posicao == numero:
            posicao_encontrada = contador
        contador+=1
    if posicao_encontrada >= 0:
        print(f'Encontrado {numero} na posição {posicao_encontrada}')
    else:
        print(f'{numero} não encontrado')   

    #2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
    #numerada.
    letras = []
    for posicao in range(10):
        letras.append(chr(random.randrange(65,91)))
        print(f'[{posicao}] = {letras[posicao]}')

    #3. Construa uma programa que armazene 15 números em uma lista e imprima
    #uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
    numeros = []
    for posicao in range(15):
        numeros.append(random.randrange(1,100))
        resultado = 'PAR' if numeros[posicao] % 2 == 0 else 'IMPAR'
        print(f'[{posicao}] = {numeros[posicao]}\t{resultado}')

    #4. Faça um programa que armazene 8 números em uma lista e imprima todos os
    #números. Ao final, imprima o total de números múltiplos de seis.
    print(numeros)
    multiplos_6 = []
    for numero in numeros:
        if numero % 6 == 0:
            multiplos_6.append(numero)
    print(multiplos_6)
    
    #5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
    #e armazene a média arredondada. Armazene também a situação do aluno: 1-
    #Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
    #contendo as notas, a média e a situação de cada aluno em formato tabulado.
    #Utilize quantas listas forem necessárias para armazenar os dados.

    # Solução utilizando diversas listas
    nomes = []
    notas1 = []
    notas2 = []
    medias = []
    situacoes = []
    qtde_alunos = 3
    for cont in range(qtde_alunos):
        nomes.append(input('Nome: '))
        notas1.append(round(float(input('Nota1: ')), 1))
        notas2.append(round(float(input('Nota2: ')), 1))
        medias.append(round((notas1[cont]+notas2[cont])/2, 1))
        situacao = 'APROVADO' if medias[cont] >= 6 else 'REPROVADO'
        situacoes.append(situacao)
    
    for cont in range(qtde_alunos):
        print(f'{nomes[cont]}\t{notas1[cont]}\t{notas2[cont]}\t{medias[cont]}\t{situacoes[cont]}')

    # Solução utilizando uma única lista
    alunos = []
    for cont in range(qtde_alunos):
        aluno = {}
        aluno['nome'] = input('Nome: ')
        aluno['n1'] = round(float(input('Nota1: ')), 1)
        aluno['n2'] = round(float(input('Nota2: ')), 1)
        aluno['media'] = round((aluno['n1']+aluno['n2'])/2, 1)
        aluno['situacao'] = 'APROVADO' if aluno['media'] >= 6 else 'REPROVADO'       
        alunos.append(aluno)

    alunos_ordenado = sorted(alunos, key=lambda a: a['media'], reverse=True)

    for aluno in alunos_ordenado:
        print(f"{aluno['nome']}\t{aluno['n1']}\t{aluno['n2']}\t{aluno['media']}\t{aluno['situacao']}")
    
    #6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
    #e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
    #listagem numerada com o salário e o novo salário. Declare quantas listas forem
    #necessárias.

funcionarios = []


def cadastrar_funcionario():
    print('CADASTRO DE FUNCIONARIO')
    funcionario = {}
    funcionario['nome'] = input('Nome:')
    funcionario['salario_bruto'] = float(input('Salbário Bruto: '))
    return funcionario

def menu():
    tela = '''
        [1] - Cadastrar
        [0] - sair
    '''
    opcao = -1
    while (opcao!=0):
        print(tela)
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            funcionario = cadastrar_funcionario()
            funcionarios.append(funcionario)
        else:
            if opcao!=0:
                print('Opção Inválida! Tente novamente.')

def reajustar_salarios(pessoas, reajuste):
    for pessoa in pessoas:
        pessoa['salario_bruto'] = pessoa['salario_bruto'] * (1+reajuste/100)

def exibir_salarios(pessoas):
    for pessoa in pessoas:
        print(f"{pessoa['nome']}\t{pessoa['salario_bruto']}")

menu()
print('Salários antes do Reajuste')
exibir_salarios(funcionarios)
reajustar_salarios(funcionarios,8)
print('Salários após o Reajuste')
exibir_salarios(funcionarios)



    #7. Crie umprograma que leia o preço de compra e o preço de venda de 100 mercadorias
    #(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
    #proporcionam:
    #• lucro < 10%
    #• 10% <= lucro <= 20%
    #• lucro > 20%
def compra_venda():
	for cont in range(1,101):	
		compra = float(input('Qual o preço de compra?\n'))
		venda = float(input('Qual o preço de venda?\n'))
mercadoria = [compra,venda]

	    
    
    
    

    #8. Construa um programa que armazene o código, a quantidade, o valor de compra
    #e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
    #somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.

    #9. Faça um programa que leia dois conjuntos de números inteiros, tendo
    #cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
    #conjuntos.

    #10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
    #cujos valores são os fatoriais da lista original.

    #11. Construa um programa que leia dados para uma lista de 100 elementos inteiros.
    #Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
    #média dos elementos da lista.

    #12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
    #de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
    #permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
    #quantidade de lugares desejados. O programa deverá informar se foi possível
    #realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
    #emitir uma mensagem. O programa deve terminar quando o usuário digitar
    #o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
    #ocupados.

    #13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
    #O programa deve permitir cadastrar o número de 10 voos e definir a
    #quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
    #pedidos de reserva, constituídos do número da carteira de identidade do cliente e
    #do número do voo desejado. Para cada cliente, verificar se há possibilidade no
    #voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
    #o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
    #avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
    #desejado indica o término da leitura de reservas.

    #14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
    #deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
    #elemento da primeira lista.

    #15. Faça um programa que leia e armazene vários números, até digitar o número
    #0. Imprimir quantos números iguais ao último número foram lidos. O limite de
    #números é 100.

    #16. Crie um programa para ler um conjunto de 100 números reais e informe:
    #• quantos números lidos são iguais a 30
    #• quantos são maior que a média
    #• quantos são iguais a média

    #17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
    #um vetor e os imprima ao contrário da ordem de leitura.

    #18. Faça um programa que permita entrar com 20 valores numéricos, 
    # em que podem existir vários elementos repetidos. Gere
    #uma lista ordenada que terá apenas os elementos não repetidos.

    #19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
    #um programa que permita buscar pelo código e imprimir o telefone.

    #20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
    #para a menor nota e imprima uma relação contendo todas as matrículas e médias.

