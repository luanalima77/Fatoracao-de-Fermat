#Biblioteca de matemática do Python.
import math

#O usuário digita um número.
numero_digitado = int(input("Digite um número: " ))

#Função para realizar a fatoração de Fermat
def fermat_fatorar(n):
    #Verificando se o número é ímpar.
    if n % 2 != 0:
         #Primeiro fator: parte inteira da raiz quadrada de n.
        a = math.isqrt(n)

        #Verificação para que o a seja sempre maior que o n, para evitar uso de números negativos.
        if a*a < n:
            a += 1 

        #Calculando o fator b2 (que depois será armazenado em b). Além disso, foi criada uma variável para calcular o número de iterações.
        b2 = (a*a) - n
        iteracoes = 1

        #Enquanto b2 não for quadrado perfeito, o a vai sendo incrementado e o cálculo é realizado novamente. A iteração também aumenta em uma unidade.
        while int(math.isqrt(b2)) ** 2 != b2:
            iteracoes += 1
            a = a + 1
            b2 = (a*a) - n
            
        #Se chegamos a b2 como quadrado perfeito, armazenamos ele em uma variável chamada b
        b = math.sqrt(b2)
        fator_primo_1 = int(a - b)
        fator_primo_2 = int(a + b)

        #Retornando os fatores primos e o número de iterações.
        return f"\nPrimeiro fator primo: {fator_primo_1}\nSegundo fator primo: {fator_primo_2}\nQuantidade de iterações feitas: {iteracoes}"
    
    #Se o número for par, aparece a mensagem de que ele pode ser fatorado no número primo 2.
    else:
        return "O número digitado é par e pode ser fatorado no número primo 2"

#Mostrando os fatores primos e o número de iterações no terminal.
print(fermat_fatorar(numero_digitado))
