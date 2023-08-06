## Funções
---

Uma função é um bloco que código que só é executado quando chamado. No Python, funções são objetos de primeira classe. O que significa dizer que uma função é tratada da mesma forma que qualquer variável e pode ser:

- Criada durante a execução de um programa
- Atribuida a uma variável ou a um elemento em uma estrutura de dados
- Passada como argumento para uma função
- Devolvida como o resultado de uma função

### Como declarar e executar uma função?

No python, declarações de funções são dadas pela palavra reservada ***`def`***

```python 
def hello(): 
    print("Olá Mundo!")
```

Agora, para executar sua função basta chamá-la no seu código ou no interpretador python. 
```python
hello()
```
![ola_mundo](screenshots\functions\ola_mundo.png)


### Argumentos e Parâmetros
---
É possível passar valores para sua função, esses valores são chamados de argumentos e parâmetros. 
Parâmetros são variáveis declaradas no momento de declaração da função e esperam receber algum valor na chamada da função. Esse valor esperado na chamada da função é chamado de argumento.

```python
def hello(x):
    print("Olá, " + x)
```

Você pode nomear esses parametros de forma que torne descritivo o que ele é, para evidenciar qual o uso dele na função. 

```python
def hello(nome):
    print("Olá, " + nome)
```

Ou seja, o parâmetro da função hello é a variável nome, enquanto o argumento é o valor passado na chamada da função, no exemplo a seguir, o argumento é a string João.

![hello_joao](screenshots\functions\hello_joao.png)


As funções também podem retornar valores, é possível receber argumentos, executar operações com esses argumentos e devolver o resultado dessas operações.

```python 
def soma(valor1, valor2):
    return valor1 + valor2

def potencia(base, expoente):
    return base**expoente
```

>Não há quantidade máxima de argumentos a serem passados, contudo caso haja uma grande quantidade de argumentos, há a possibilidade de dificultar a legibilidade da função e talvez seja o momento de refatorar a funcionalidade. 

### Função como retorno de função
----
Como comentado anteriormente, também é possível retornar funções como resposta da chamada de funções, o que torna possível a execução de funções chamadas recursivas (funções que chamam a si mesmas). Como por exemplo o cálculo do fatorial de um número.

O fatorial de um número inteiro não negativo "n" é o produto de todos os números inteiros positivos de 1 a "n". É representado por "n!" e é definido da seguinte forma:

`n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`

Agora, vamos expressar a função fatorial em python:

```python
def fatorial(numero):
    if numero == 1:
        return 1
    else 
        numero_anterior = numero - 1
        return numero * fatorial (numero_anterior)
```
Quando se escreve uma função é importante levar em consideração os argumentos que essa função pode receber e se previnir quanto a erros. Na função fatorial anterior, está tudo certo para o caminho feliz, mas temos o caso de passar um número negativo, ou não passar um número, ou até mesmo passar o valor 0. Então, vamos tratar a nossa função para esses casos: 

```python 
#Criamos uma função auxiliar para verificar se o número passado é um inteiro
def verifica_inteiro(numero):
    try:
        resultado = numero + 1
        return True
    except TypeError:
        return False

def fatorial(numero):
    # Utilizamos a chamada da função verifica_inteiro que nós criamos pra garantir que o argumento numero é um inteiro. E adotamos a tecnica de early return, para impedir o código continue a sua execução com um valor inadequado na variável numero. 
     if not verifica_inteiro(numero) or numero < 0:
        print("O fatorial é definido apenas para números inteiros não negativos.")
        return
    # Caso base da recursão, onde 0! e 1! possuem o mesmo valor, 1.    
    if numero == 1 or numero == 0:
        return 1
    # Cálculo da recursão, onde o resultado de n! é igual a n * (n-1)!
    return numero * fatorial(numero - 1)
```
 
 O que acontece no cálculo recursivo da função é que o valor a ser calculado está sendo adicionado à pilha de execução, de forma que o cálculo de fatorial(5) seria dado pelas chamadas consecutivas da função de tal forma:
 ```python
fatorial(5) = 5 * fatorial (4) 
# adiciona a expressão anterior à pilha de execução
fatorial(4) = 4 * fatorial (3)
# adiciona a expressão anterior à pilha de execução
fatorial(3) = 3 * fatorial(2)
# adiciona a expressão anterior à pilha de execução
fatorial(2) = 2 * fatorial(1)
# adiciona a expressão anterior à pilha de execução
fatorial(1) = 1
# Aqui o caso base da recursão é atingido, e as expressões da pilha de execução começam a ser removidas para terem seus valores substituídos. 

# Agora, o ultimo elemento inserido da pilha é removido e substituido pelo resultado da expressão anterior, até que a pilha esteja vazia.
fatorial(2) = 2 * fatorial(1) = 2 * 1 = 2
# O proximo elemento da pilha é removido e é realizada a substituição
fatorial(3) = 3 * fatorial(2) = 3 * 2 * fatorial(1) = 3 * 2 * 1 = 6
# Assim, continuamos removendo as expressões da pilha e calculando 
fatorial(4) = 4 * fatorial(3) = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1) = 4 * 3 * 2 * 1 = 24 
# Por fim, é removido o ultimo elemento da pilha
fatorial(5) = 5 * fatorial(4) = 5 * 4 * fatorial(3) = 5 * 4 * 3 * fatorial(2) = 5 * 4 * 3 * 2 * fatorial(1) = 5 * 4 * 3 * 2 * 1 = 120
 ```

@TODO talvez adicionar um gif com a operação na pilha




## Funções Embutidas (Built in)
---
As funções embutidas em Python são funções que estão disponíveis diretamente no interpretador Python e não requerem a importação de módulos adicionais para serem usadas. Elas são fornecidas pelo próprio Python como parte do seu conjunto padrão de funcionalidades e oferecem recursos essenciais e comuns para manipulação de dados, cálculos matemáticos, operações com strings, iterações, conversões de tipos, entre outros.

Aqui estão algumas das funções embutidas em Python:

### A
- `abs()`: Retorna o valor absoluto de um número.
- `aiter()`: Retorna um objeto iterável assíncrono.
- `all()`: Retorna True se todos os elementos de uma sequência são verdadeiros, caso contrário, retorna False.
- `any()`: Retorna True se algum dos elementos de uma sequência é verdadeiro, caso contrário, retorna False.
- `anext()`: Retorna o próximo valor de um objeto iterável assíncrono.
- `ascii()`: Retorna uma representação da string usando a tabela ASCII.

### B
- `bin()`: Converte um número inteiro em uma representação binária.
- `bool()`: Converte um valor em um valor booleano (True ou False).
- `breakpoint()`: Introduz um ponto de interrupção para depuração.
- `bytearray()`: Cria um objeto bytearray (sequência de bytes modificável).
- `bytes()`: Converte um objeto em uma sequência de bytes.

### C
- `callable()`: Verifica se um objeto pode ser chamado como uma função.
- `chr()`: Retorna o caractere Unicode correspondente a um código inteiro.
- `classmethod()`: Transforma um método em um método de classe.
- `compile()`: Compila código Python em um objeto código ou AST.
- `complex()`: Cria um número complexo a partir de partes reais e imaginárias.

### D
- `delattr()`: Remove um atributo de um objeto.
- `dict()`: Cria um dicionário (coleção de pares chave-valor).
- `dir()`: Retorna a lista de nomes de atributos de um objeto.
- `divmod()`: Retorna o resultado da divisão e o resto como uma tupla.

### E
- `enumerate()`: Retorna uma sequência de tuplas com índice e valor de uma sequência.
- `eval()`: Avalia uma expressão Python de uma string.
- `exec()`: Executa código Python dinamicamente.

### F
- `filter()`: Filtra elementos de uma sequência com base em uma função de retorno booleano.
- `float()`: Converte um valor em um número de ponto flutuante.
- `format()`: Formata uma string substituindo campos delimitados por chaves por valores fornecidos.
- `frozenset()`: Cria um conjunto imutável (frozenset).

### G
- `getattr()`: Retorna o valor de um atributo de um objeto.
- `globals()`: Retorna o dicionário de símbolos globais.

### H
- `hasattr()`: Verifica se um objeto tem um atributo específico.
- `hash()`: Retorna o valor hash de um objeto.
- `help()`: Exibe informações de ajuda sobre um objeto ou função.
- `hex()`: Converte um número inteiro em uma representação hexadecimal.

### I
- `id()`: Retorna a identificação única (endereço de memória) de um objeto.
- `input()`: Permite a leitura de dados de entrada fornecidos pelo usuário.
- `int()`: Converte um valor em um número inteiro.
- `isinstance()`: Verifica se um objeto é uma instância de uma classe específica.
- `issubclass()`: Verifica se uma classe é subclasse de outra.
- `iter()`: Retorna um iterador para um objeto.

### L
- `len()`: Retorna o tamanho (número de elementos) de uma sequência, como strings, listas, tuplas, etc.
- `list()`: Cria uma lista (sequência modificável).
- `locals()`: Retorna o dicionário de símbolos locais.

### M
- `map()`: Aplica uma função a todos os itens de uma ou mais sequências.
- `max()`: Retorna o maior valor de uma sequência ou de dois ou mais argumentos.
- `memoryview()`: Cria um objeto de visualização da memória de um objeto.
- `min()`: Retorna o menor valor de uma sequência ou de dois ou mais argumentos.

### N
- `next()`: Retorna o próximo elemento de um iterador.

### O
- `object()`: Retorna um novo objeto vazio.
- `oct()`: Converte um número inteiro em uma representação octal.
- `open()`: Abre um arquivo para leitura, escrita ou outras operações.
- `ord()`: Retorna o valor Unicode de um caractere.

### P
- `pow()`: Retorna a potência de um número.
- `print()`: Exibe mensagens e valores na saída padrão.
- `property()`: Retorna um atributo de propriedade.

### R
- `range()`: Cria uma sequência de números inteiros em um intervalo especificado.
- `repr()`: Retorna uma representação de string de um objeto.
- `reversed()`: Retorna uma sequência reversa de uma sequência dada.
- `round()`: Arredonda um número para um número inteiro ou casas decimais específicas.

### S
- `set()`: Cria um conjunto (coleção de elementos únicos).
- `setattr()`: Define um valor para um atributo de um objeto.
- `slice()`: Retorna um objeto fatia que pode ser usado para acessar uma parte de uma sequência.
- `sorted()`: Retorna uma nova lista ordenada a partir dos elementos de uma sequência.
- `staticmethod()`: Transforma um método em um método estático.
- `str()`: Converte um objeto em uma representação de string.
- `sum()`: Retorna a soma dos elementos de uma sequência.
- `super()`: Retorna um objeto proxy que delega chamadas a métodos para uma classe pai.

### T
- `tuple()`: Cria uma tupla (sequência imutável).
- `type()`: Retorna o tipo de dado de um objeto.

### V
- `vars()`: Retorna o dicionário de atributos de um objeto.

### Z
- `zip()`: Combina elementos de duas ou mais sequências em uma sequência de tuplas.

### _
- `__import__()`: Importa um módulo em tempo de execução.

> Essas são as funções embutidas disponíveis em Python. O conjunto completo de funções embutidas e suas explicações detalhadas podem ser encontradas na [documentação oficial do Python](https://docs.python.org/3/library/functions.html), que foi fonte para essa parte da apostila.


## Modificando nossas funções para utilizar funções embutidas
---
Agora que conhecemos essas funções embutidas, as nossas funções podem ser modificadas para utiliza-las e outras se tornam desnecessárias, como a de cálculo da soma e da potência.

Primeiro, podemos melhorar a nossa função hello() e imprimir uma saudação personalizada

![hello_maria](screenshots\functions\ola_maria.png)

Podemos tambem descartar a função potencia e soma, e utilizar as funções built in

![builtin_sum](screenshots\functions\built_in_sum.png)

![builtin_pow](screenshots\functions\built_in_pow.png)


Podemos modificar nossa função fatorial pra remover a função de verificação de inteiro e utilizar a função built in isinstance
```python 
def fatorial(numero):
    # Utilizamos a chamada da função isinstance, pra garantir que o argumento numero é um inteiro. E adotamos a tecnica de early return, para impedir o código continue a sua execução com um valor inadequado na variável numero. 
     if not isinstance(numero,int) or numero < 0:
        print("O fatorial é definido apenas para números inteiros não negativos.")
        return
    # Caso base da recursão, onde 0! e 1! possuem o mesmo valor, 1.    
    if numero == 1 or numero == 0:
        return 1
    # Cálculo da recursão, onde o resultado de n! é igual a n * (n-1)!
    return numero * fatorial(numero - 1)
```

Ou ainda, podemos importar um módulo e utilizar as funções desses módulos, como por exemplo, a função fat do módulo math, abstraindo nossa implementação da função de cálculo do fatorial.

![math_factorial](screenshots\functions\math_factorial.png)