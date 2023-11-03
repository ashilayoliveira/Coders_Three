# Função para executar a divisão
def executar_divisao(a, b):
    return a / b

# Variáveis para armazenar os valores informados pelo usuário
var1 = float(input("Digite o primeiro valor: "))
var2 = float(input("Digite o segundo valor: "))

# OB JU: Verificação da var 2 faltou um if


if var2 <= 0:
    print("O segundo valor não pode ser aceito o valor zero, nem um valor negativo.")
    valor2 = float(input("Digite um novo valor para o segundo valor: "))

# executar a divisão e exibir o resultado
resultado = executar_divisao(var1, var2)
print("O resultado da divisão é:", resultado)


# Função para criar a bomba relógio
def bomba_relogio():
    import time

    # Contagem regressiva de 30 a 0
    for i in range(30, -1, -1):
        # Limpar a tela (opcional)
        print("\033[H\033[J")
        
        # Escrever o número da contagem regressiva
        print(f"{i}")
        
        # Aguardar 1 segundo
        time.sleep(1)
    
    # Exibir "EXPLOSÃO" após a contagem regressiva terminar
    print("\033[H\033[J")
    print("EXPLOSÃO")

# Executar a função bomba_relogio
bomba_relogio()

# JU tirei for i in range(10, 0, -1):
    #print(i, end=", ")

#Calculo do algoritmo

contador = 0
acumulador = 0

#JU: adicionei contador += 1

for i in range(15, 101):
    acumulador += i
    contador += 1

# Calcular a média aritmética
media_aritmetica = acumulador / contador

# A média dos números entre 15 e 100 é: 64.5

print("A média aritmética dos números entre 15 e 100 é:", media_aritmetica)

# Solicitar números ao usuário
num1 = int(input("Informe o primeiro número inteiro: "))
num2 = int(input("Informe o segundo número inteiro: "))

# Verificar se num1 é menor que num2
while num1 >= num2:
    print("O primeiro número deve ser menor que o segundo. Por favor, tente novamente.")
    num1 = int(input("Informe o primeiro número inteiro: "))
    num2 = int(input("Informe o segundo número inteiro: "))

# Variáveis para armazenar a média aritmética e o total
acum = 0
cont = 0

# Loop para calcular a média aritmética e a soma dos números entre num1 e num2
for i in range(num1, num2 + 1):
    acum += i
    cont += 1

# Calcular a média aritmética
media_aritmetica = acum / cont

#Ju: Exibir na tela 
print("Média aritmética", media_aritmetica)
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def ler_notas():
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    media = calcular_media(nota1, nota2)
    return media

def main():
    alunos_aprovados = 0

    while True:
        media = ler_notas()

        if media >= 9.5:
            alunos_aprovados += 1

        resposta = input("Calcular a média de outro aluno Sim/Não? ")
        if resposta.lower() != "s":
            break

    print(f"A quantidade de alunos aprovados é: {alunos_aprovados}")

if __name__ == "__main__":
    main()

N = int(input("Informe o valor de N: "))

for i in range(1, N + 1):
    print(i)

# ju decarta isso: N = int(input("Informe o valor de N: "))

#for i in range(1, N + 1):
 #   print(i)

def main():
    # Ler o valor N
    N = int(input("Informe o valor de N: "))

    # Verificar se N é maior que 100
    if N > 100:
        # Imprimir os 10 primeiros números inteiros maiores que N
        for i in range(N + 1, N + 11):
            print(i)
    else:
        print("N deve ser maior que 100")

if __name__ == "__main__":
    main()

def tabuada(num):
    for i in range(1, num + 1):
        print(f"{num} x {i} = {num * i}")

def main():
    N = int(input("Informe o valor de N: "))

    for i in range(1, N + 1):
        print(f"\nTabuada de {i}")
        tabuada(i)

if __name__ == "__main__":
    main()

valores = []
cont_dentro = 0
cont_fora = 0

for i in range(10):
    valor = int(input(f"Informe o valor {i + 1}: "))
    valores.append(valor)

for valor in valores:
    if 24 <= valor <= 42:
        cont_dentro += 1
    else:
        cont_fora += 1

print(f"{cont_dentro} valores estão entre os números 24 e 42.")
print(f"{cont_fora} valores estão fora deste intervalo.")
