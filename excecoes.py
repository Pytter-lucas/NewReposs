try:
    x = int(input('Digite um valor numérico: '))
    y = int(input('Digite outro valor numérico: '))
    resultado = x/y
    print(resultado)
except ValueError: # śo ira ocorrer em caso de valores não inteiros
    print('Eita usuário, vc digitou um valor que não é um inteiro, preste atenção!!!')
except ZeroDivisionError:# só irá ocorrer se y for igual a zero (0)
    print('Não pode haver divisão de um número por zero (0)!')
except(exc):
    print('Erro inesperado, contate o administrador do sistema!')
    print(exc)
else: # só irá ocorrer se não houver nenhum na execução
    print('Parabéns usuário, vc é demais, nao errou nada!!!')
finally: # sempre irá ocorrer independentemente de errou ou sucesso
    print('Fim do programa!')

x = 0
y = 0
erro = True
while erro == True:
    try:
        x = int(input('Digite um valor numérico para X: '))
        erro = False
    except ValueError:
        print('Eita usuário, vc digitou um valor que não é um inteiro, preste atenção')
        erro = True

erro = True
while erro == True:
    try:
        y = int(input('Digite um valor numérico para Y: '))
        if y == 0:
            raise Exception('Cara, não existe valor 0 para Y')
        erro = False
    except ValueError:
        print('Eita usuário, vc digitou um valor que não é um inteiro, preste atenção')
        erro = True
    except:
        erro = True
try:
    resultado = x/y
except ZeroDivisionError:
    print('Não pode haver divisão de um número por zero (0)!')
else:
    print(resultado)