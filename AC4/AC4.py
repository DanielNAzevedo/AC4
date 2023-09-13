"""
Programação estruturada
AC4
Questão 1
Elabore uma função e_primo(num) que retorna se um número num é primo ou não. Caso num não seja primo, liste todos os números pelos quais num é divisível.
"""
def e_primo(num):
    primo = True

    for div in range(2, num):
        if num % div == 0:
            print(div)
            primo = False
        
    if primo == True:
            print("True")
    else:
        print("False") 
e_primo(6)

"""
Questão 2
Faça um programa que receba o valor de uma dívida e mostre as opções de parcelamento. O resultado final deve conter as opções de 1, 3, 6, 9 ou 12 parcelas, e o percentual de juros para cada parcela deve ser determinado conforme a primeira tabela, abaixo. O relatório com as opções de pagamento deve conter os seguintes dados: valor dos juros, valor total da dívida (incluindo juros), quantidade de parcelas e valor da parcela. A segunda tabela, abaixo, mostra um exemplo de como o resultado deve ser exibido. No momento, não é necessário formatar os valores.
"""
valor = 1000

num_parcelas = 1

def taxa_juros(num_parcelas):

    if num_parcelas == 1:
        percentual = 0
    
    if num_parcelas == 3:
        percentual = 0.10
    
    if num_parcelas == 6:
        percentual = 0.15
    
    if num_parcelas == 9:
        percentual = 0.20
    
    if num_parcelas == 12:
        percentual = 0.25 
    return percentual 

def conta(valor, num_parcelas):
    juros_conta = valor * taxa_juros (num_parcelas)
    valor_total =  taxa_juros + valor 
    parcela = valor_total / num_parcelas
    print(juros_conta, valor_total, num_parcelas, parcela)

def opcoes_divida(divida):
    print("Valor dos juros Valo0r total Quantidade de parcelas valor de parcela")
    print("0 R$", divida, "1R%", divida)
    for n in range(3, 13, 3):
        conta(divida, n)
div = float(input("Diga a sua divida:"))
opcoes_divida(div)


"""
Questão 3
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
"""
n = 1
c1 = 0
c2 = 0
c3 = 0
c4 = 0
while n > 0:
    n = int(input("Digite um número"))
    if n >= 0 and n <= 25:
        c1 = c1 + 1
    elif n >= 26 and n <= 50:
        c2 = c2 + 1
    elif n >= 51 and n <= 75:
        c3 = c3 + 1
    elif n >= 76 and n <= 100:
        c4 = c4 + 1
print("A quantidade de números entre 0 e 25 é: ", c1, ", entre votos 26-50 é: ", c2, ", entre votos 51-75 é: ", c3, ", e entre votos 76-100 é: ", c3)
