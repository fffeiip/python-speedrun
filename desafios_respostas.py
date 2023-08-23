# Desafio 1: Calculadora Simples
def calculadora_simples():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    op = input("Escolha a operação (+, -, *, /): ")

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Operação inválida!")

# Desafio 2: Conversor de Temperatura
def conversor_temperatura():
    temp = float(input("Digite a temperatura: "))
    tipo = input("É Celsius (C) ou Fahrenheit (F)? ")

    if tipo == "C":
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C é igual a {fahrenheit}°F")
    elif tipo == "F":
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F é igual a {celsius}°C")
    else:
        print("Tipo inválido!")

# Desafio 3: Gerador de Senhas Aleatórias
def gerador_senhas():
    import random
    import string

    tamanho = int(input("Digite o tamanho da senha: "))
    senha = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=tamanho))
    print(senha)

# Desafio 4: Calculadora de Idade
def calculadora_idade():
    ano_atual = 2023
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = ano_atual - ano_nascimento
    print(f"Sua idade é: {idade} anos")

# Desafio 5: Verificador de Número Primo
def verificador_primo():
    num = int(input("Digite um número: "))
    primo = True

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(f"{num} é primo!")
    else:
        print(f"{num} não é primo!")

# Desafio 6: Calculadora de Fatorial
def calculadora_fatorial():
    num = int(input("Digite um número: "))
    fatorial = 1

    for i in range(1, num + 1):
        fatorial *= i

    print(f"Fatorial de {num} é {fatorial}")

# Desafio 7: Jogo da Adivinhação
def jogo_adivinhacao():
    import random

    numero_secreto = random.randint(1, 100)
    tentativa = int(input("Adivinhe o número entre 1 e 100: "))

    while tentativa != numero_secreto:
        if tentativa < numero_secreto:
            print("Mais alto!")
        else:
            print("Mais baixo!")
        tentativa = int(input("Tente novamente: "))

    print("Parabéns! Você acertou!")

# Desafio 8: Conversor de Moedas
def conversor_moedas():
    valor_reais = float(input("Digite o valor em reais: "))
    taxa_cambio = 5.0
    valor_dolar = valor_reais / taxa_cambio
    print(f"R${valor_reais} é igual a ${valor_dolar}")

# Desafio 9: Calculadora de Média
def calculadora_media():
    numeros = input("Digite os números separados por espaço: ").split()
    media = sum(map(float, numeros)) / len(numeros)
    print(f"A média é: {media}")

# Desafio 10: Verificador de Palíndromo
def verificador_palindromo():
    texto = input("Digite uma palavra ou frase: ").replace(" ", "").lower()
    if texto == texto[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo!")

# Para executar qualquer desafio, basta chamar a função correspondente.
# Por exemplo: calculadora_simples()
