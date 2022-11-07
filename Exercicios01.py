#1. Faça um programa que imprima o seu nome.
print('Pytter Lucas Da Silva')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
print(30*27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
media = 5 + 8 + 12
print(media/3)

#4. Faça um programa que leia e imprima um número inteiro.
num1 = int(input('Insira um número inteiro: ')) 
print(num1)

#5. Faça um programa que leia dois números reais e os imprima.
num1 = float(input('Insira o primeiro número real: '))
num2 = float(input('Insira o segundo número real: '))
print('Os números apresentados foram: ',num1,' e  ',num2)

#6. Faça umprograma que leia umnúmero inteiro e imprima o seu antecessor e o seu sucessor.
numero = int(input('Digite um número inteiro qualquer: '))
print(f'Seu antecessor: {numero-1}, e o seu sucessor: {numero+1}')

#7. Faça umprograma que leia o nome o endereço e o telefone de um cliente e ao final, imprima esses dados.
nome = (input('Informe seu nome: '))
endereco = (input('Informe seu endereço: '))
telefone = (input('Informe seu telefone: '))
print('O nome do cliente é ',nome,' ele fica localizado no 2',endereco,' seu telefone pra contato é ',telefone)

#8. Faça umprograma que leia dois números inteiros e imprima a subtração deles.
num1 = float(input('insira o primero número: '))
num2 = float (input('Insira o segundo número: '))
print(f'O resultado da subtração foi: {num1 - num2}')

#9. Faça um programa que leia umnúmero real e imprima ¼ deste número.
num1 = float(input('Apresente um número real: '))
print(f'Um quarto deste número é : {num1 / 4}')

#10. Faça umprograma que leia três números reais e calcule a média aritmética destes números. Ao final, o programa deve imprimir o resultado do cálculo.
num1 = float(input('Informe a primeira nota: '))
num2 = float(input('Informe a segunda nota: '))
num3 = float(input('Informe a terceira nota: '))
media = (num1+num2+num3)
print(f'a média aritmética obtida foi: {media/3}')

#11. Faça umprograma que leia dois números reais e calcule as quatro operações básicas entre estes dois números, adição, subtração,multiplicação e divisão. Ao final, o programa deve imprimir os resultados dos cálculos.
num1 = float(input('Apresente o 1º número para realizamos as operações: '))
num2 = float(input('Apresente o segundo: '))
print(f'SOMA: {num1+num2}')
print(f'SUBTRAÇÃO: {num1-num2}')
print (f'DIVISÃO: {num1/num2}')
print(f'MULTIPLICAÇÃO: {num1*num2}')

#12. Faça um programa que leia um número real e calcule o quadrado deste número. Ao final, o programa deve imprimir o resultado do cálculo.
num1 = float(input('Informe um número real: '))
print(f'O quadrado deste número é: {num1**2}') 

#13. Faça umprograma que leia o saldo de uma conta poupança e imprima o novo saldo, considerando umreajuste de 2%.
num1 = float(input('Usúario informe seu saldo: '))
porce = 2 % num1
num2 = porce + num1
print('Ouve um reajuste em seu saldo, de R$:',num1,' reais, para R$:',num2,' reais. Foi um reajuste de 2%, que foi de: ',porce)

#14. Faça umprograma que leia a base e a altura de um retângulo e imprima o perímetro (base + altura) e a área (base * altura).
num1 = float(input('Informe a base do retângulo: '))
num2 = float(input('informe a altura: '))
if num1 == num2:
    print('Um retângulo não possui lados iguais!!!')
else:
    print(f'O perimetro é: {num1+num2}cm² e a aréa de seu retângulo é: {num1*num2}cm²')
    
#15. Faça um programa que leia o valor de um produto, o percentual do desconto desejado e imprima o valor do desconto e o valor do produto subtraindo o desconto.
produto = float(input('Informe o valor do produto: '))
desconto = float(input('Qual o percentual de desconto desejado? '))
descontofinal = desconto % produto
produtofinal = produto - descontofinal
print('O seu desconto foi de R$',descontofinal,'reais agora o senhor(a) irá pagar: R$',produtofinal,'Reais.')
#16. Faça um programa que calcule o reajuste do salário de um funcionário. Para isso, o programa deverá ler o salário atual do funcionário e ler o percentual de reajuste. Ao final imprimir o valor do novo salário.
salario = float(input('Qual o sálario que o funcionário recebe atualmente? '))
reajuste = float(input('Qual o percentual de reajuste salarial? '))
reajustefinal = reajuste % salario
print(f'Salário atualizado: R$:{salario+reajustefinal} reais.')
 
#17. Faça um programa que calcule a conversão entre graus centígrados e Fahrenheit. Para isso, leia o valor em centígrados e calcule com base na fórmula a seguir. Após calcular o programa deve imprimir o resultado da conversão.
#F = (9 x C +160) / 5
cel = float(input('Usúario, me informe os graus em celsius? '))
fah = (9 * cel) + 160
print ('A conversão foi realizado com sucesso!!!')
print (f'{fah/5} Graus Fahrenheit')

#18. Faça umprograma que calcule a quantidade de litros de combustível consumidos em uma viagem, sabendo-se que o carro tem autonomia de 12 km por litro de combustível. O programa deverá ler o tempo decorrido na viagem e a velocidade média e aplicar as fórmulas:
#D = T x V       L = D / 12
#Em que:
#• D = Distância percorrida em horas
#• T = Tempo decorrido
#• V = Velocidade média
#• L = Litros de combustível consumidos
#Ao final, o programa deverá imprimir a distância percorrida e a quantidade de litros consumidos na viagem.
tempo = float(input('Informe o tempo percorrido: '))
velocidade = float(input('informe a velocidade em média mantida: '))
d = tempo * velocidade
l = d / 12
print('A distância percorrida',d,'KM, e foram consumidos',l,'KM/L.')

#19. Faça um programa que calcule o valor de uma prestação em atraso. Para isso, o programa deve ler o valor da prestação vencida, a taxa periódica de juros e o período de atraso. Ao final, o programa deve imprimir o valor da prestação atrasada, o período de atraso, os juros que serão cobrados pelo período de atraso, o valor da prestação acrescido dos juros. Considere juros simples.
parcela = float(input('Informe qual o valor da parcela: '))
mes = float(input('Quantos meses a parcela está em atraso: '))
print('Será agregados 2% de juros simples ao mês.')
juros = (parcela % 2) * mes
valorfinal = parcela + juros
print('A prestação estava no valor R$:',parcela,'reais.\n Foram',mes,' mês(es) de atraso.\n Então sua parcela foi reajustada para este valor. R$:',valorfinal )
#20. Faça um programa que efetue a apresentação do valor da conversão em real (R$) de umvalor lido em dólar (US$). Para isso, será necessário também ler o valor da cotação do dólar.
dolar = 5.12
real = float(input('Quantos reais você tem para realizamos a conversão: '))
conversao = real/dolar
print(f'A cotação do dólar está em US$:',dolar,'. Conversão realizada com sucesso: US$:',conversao)