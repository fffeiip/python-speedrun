## Funções

Uma função é um bloco que código que só é executado quando chamado. No Python, funções são objetos de primeira classe. O que significa dizer que uma função é tratada da mesma forma que qualquer variável e pode ser:

- Criada durante a execução de um programa
- Atribuida a uma variável ou a um elemento em uma estrutura de dados
- Passada como argumento para uma função
- Devolvida como o resultado de uma função

### Como declarar e executar uma função?

No python, declarações de funções são dadas pela palavra reservada ***`def`***

```python 
def hello(): 
    print("Hello World!")
```

Agora, para executar sua função basta chamá-la no seu código ou no interpretador python. 
```python
hello()
```

@TODO ADICIONAR PRINT do terminal 

É possível passar valores para sua função, esses valores são chamados de argumentos. Argumentos são definidos no momento de declaração da função.

```python
def hello(argumento1):
    print("Hello, " + argumento1)
```

Você pode nomear esses argumentos de forma que torne descritivo o que ele, para evidenciar qual o uso dele na função. 

```python
def hello(nome):
    print("Hello, " + nome)
```

@TODO ADICIONAR PRINT do terminal 


As funções também podem retornar valores, é possível receber argumentos, executar operações com esses argumentos e devolver o resultado dessas operações.

```python 
def soma(valor1, valor2):
    return valor1 + valor2

def exponencial(base, expoente):
    return base**expoente
```

Não há quantidade máxima de argumentos a serem passados, contudo caso haja uma grande quantidade de argumentos, há a possibilidade e dificultar a legibilidade da função e talvez seja o momento de refatorar a funcionalidade. 

Como comentado anteriormente, também é possível retornar funções como resposta da chamada de funções, o que torna possível a execução de funções chamadas recursivas (funções que chamam a si mesmas).

```python
def fatorial(numero):
    if numero == 1:
        return numero
    else 
        numero_anterior = numero - 1
        return numero * fatorial (numero_anterior)
```
Quando se escreve uma função é importante levar em consideração os argumentos que essa função pode receber e se previnir quanto a erros. Na função fatorial anterior, está tudo certo para o caminho feliz, mas temos o caso de passar um número negativo, ou não passar um número, ou até mesmo passar o valor 0. Então, vamos tratar a nossa função para esses casos: 

```python 
def fatorial(numero):
     if not isinstance(n, int) or n < 0:
        print("O fatorial é definido apenas para números inteiros não negativos.")
        return
    if numero == 1 or numero == 0:
        return 1
    return numero * fatorial(numero - 1)
```
 