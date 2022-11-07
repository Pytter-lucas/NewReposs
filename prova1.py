'''
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para:       preti.joao@ifmt.edu.br
Assunto:    Prova 1 de Laboratório de Programação 2022/2
Mensagem:   Pytter Lucas Da Silva Nobre De Lima.
Anexo:      prova1.py
'''

def main():
    '''
    Executa todass as questões
    '''

    #1. Faça um programa que leia o valor de um produto, o percentual
    #   do desconto desejado e imprima o valor do desconto e o valor
    #   do produto subtraindo o desconto. (2,0pt)
produto = float(input('Informe o valor do produto: '))
print('Lembrando que as possibilidades de desconto são de 10, 20 e 30 porcento.\n')
desconto = float(input('Informe o valor do desconto desejado: '))
if desconto == 10: 
    descontofinal = produto * 0.1
    print(f'O valor final do produto já subtraindo o desconto {produto-descontofinal}')
if desconto == 20: 
    descontofinal = produto * 0.2
    print(f'O valor final do produto já subtraindo o desconto {produto-descontofinal}')
if desconto == 30: 
    descontofinal = produto * 0.3
    print(f'O valor final do produto já subtraindo o desconto {produto-descontofinal}')
else:
    print('desconto desejado impossivél de ser concedido no momento.')
    
    #2. Faça um programa que leia 3 números e imprima o maior deles. (2,0pt)
valor1 = float(input('digite o valor1:'))
valor2 = float(input('digite o valor2:'))
valor3 = float(input('digite o valor3:'))
if (valor1 > valor2) and (valor1 > valor3):
    print(f'{valor1}')
if (valor2 > valor1) and (valor2 > valor3):
    print(f'{valor2}')
if (valor3 > valor1) and (valor3 > valor2):
    print(f'{valor3}')

    #3. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
    #   da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
    #   a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
    #   "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
    #   reprovação e as demais em prova final). (2,0pt)
nome = input('Informe seu nome: ')
nota1 = float(input('Qual foi sua nota na primeira prova: '))
nota2 = float(input('Qual foi sua nota na segunda prova: '))
if (nota1+nota2)/2 >= 7:
    print(f'O aluno {nome} está aprovado com média {(nota1+nota2)/2}\n Sua primeira nota: {nota1} e a segunda: {nota2}')
if (nota1+nota2)/2 < 3:
    print(f'O aluno {nome} está reprovado com média {(nota1+nota2)/2}\n Sua primeira nota: {nota1} e a segunda: {nota2}')
if ((nota1+nota2)/2 < 7) and ((nota1+nota2)/2 >= 3):
    print(f'O aluno {nome} foi para prova final com média {(nota1+nota2)/2}\n Sua primeira nota: {nota1} e a segunda: {nota2}')

    #4. Faça um programa que apresente um menu com 4 opções:
    #   [1] - Cadastrar
    #   [2] - Excluir
    #   [3] - Pesquisar
    #   [0] - Sair
    #   O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
    #   ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
    #   escolhida for zero (0). (2,0pt)
n = 1    
while n != 0:
    print('\n')
    print('[1] - Cadastrar\n[2] - Excluir\n[3] - Pesquisar\n[0] - sair\n')   
    n = int(input('Qual opção desejada ? '))
    if n == 1:
        print('\nCadastrada com sucesso!')
    if n == 2:
        print('\nExcluido com sucesso!')
    if n == 3:
        print ('\nPesquisado com sucesso!')
print('Chegou ao final!!!')
    #5. Faça um programa que calcule o retorno de um investimento. (2,0pt)
    #   O programa deve solicitar do usuário o:
    #   - valor que será investido;
    #   - prazo do investimento (meses);
    #   - juros mensal.
investi = float(input('Qual será o valor investido: '))
m = int(input('Qual o prazo de investimento: '))
juros = float(input('Qual o valor do juros: '))
j = juros/100
porcentagem = investi * j
for c in range(1,m+1):
    investi += + porcentagem
print(f'O resultado de seus investimentos. R$:{investi} reais.')
    
    