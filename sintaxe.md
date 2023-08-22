<h1>Sintaxe básica de Python </h1>

<h2>Variáveis e tipos de dados(inteiros, Strings, Listas, dicionários)</h2>

Em Python, assim como em outras linguagens de programação, os dados que usamos e manipulamos são armazenados em estruturas variáveis. Cada variável possui um tipo associado que define a natureza dos dados que ela pode conter.
(Explicar o que é variável)

Exemplo de definição de variável:

```python
cidade = “Recife”
```
Nesse exemplo, utilizando o operador “=”, atribuímos o valor Recife para variável de nome “cidade”.

<h3>Tipos de dados</h3>

<h3>Inteiros</h3>

Representa números inteiros, positivos ou negativos

<h3>Float</h3>

Representa números decimais

<h3>Booleano</h3>

Representa valores verdadeiros ou falsos

<h3>String</h3>

Representa uma sequência de caracteres


<h2>  Operadores(aritméticos, de comparação, lógicos) </h2>

No mundo da programação, assim como na matemática, utilizamos operadores aritméticos para realizar cálculos e operações matemáticas. 

<h3>Adição</h3>

Em Python utilizamos o operador “+” para realizar somas entre dois números.

Exemplo:

```python
soma = 3 + 5 # A variável soma vai armazenar o resultado da operação 3 + 5, que resulta em 8.
```
<h3>Subtração</h3>

Em Python utilizamos o operador “-” para realizar subtrações entre dois números

Exemplo:

```python
Subtração = 9 - 4 # A variável subtração vai armazenar o resultado da operação 9 - 4, que resulta em 5.

```
<h3>Divisão</h3>

<h3>Multiplicação</h3>

Assim como na matemática, quando realizamos operações aritméticas precisamos levar em consideração a precedência dos operadores. Temos que operações em parênteses () serão realizadas primeiramente, depois as multiplicações e divisões serão realizadas e por fim, os operadores da esquerda para a direita.

<h2>Controle de Fluxo(if, for, while)</h2>

<h3>Estruturas de Repetição</h3>
  
O if é uma estrutura fundamental em programação que permite tomar decisões em seu código.
De forma intuitiva, a expressão que estiver após a palavra if é a expressão que será testada para a condição ser verdadeira ou falsa. Ou seja, caso a expressão resulte em True, os comandos endentados após os dois pontos (:) serão executados; caso contrário, esses não serão executados.

Na linguagem Python, a sua sintaxe funciona da seguinte forma:

```python
if condição:
  #instruções do código
```

Exemplo:
```python
idade = 20

if idade >= 18:
  print("Você é maior de idade")
```

Se após o if existir o condicional else, então tudo o que estiver indentado após o else será executado quando a expressão do if não o for.

Exemplo:

```python
idade = 15

if idade >= 18:
  print("Você é maior de idade")
else:
  print("Você não é maior de idade")
```

<h3>Laçoes de repetições(For e While)</h3>

Laços de repetição são estruturas de controle que permitem executar um bloco de código várias vezes. Python fornece dois principais laços de repetição: for e while. Vamos explorar ambos em detalhes.


Utilizamos o for para executar um pedaço de código um determinado número de vezes. 
O for também é usado para iterar sobre uma sequência (lista, tupla, dicionário, conjunto ou string) ou outro objeto iterável.

A estrutura do for em python é composto pelo seguintes componentes:
A palavra reservada for
Uma variáveç
A palavra reservada in
A função range()
O código que você quer repetir

```python
for variavel in sequencia:
  # código a ser repetido
```

Exemplo:
```python
for numero in range(5):
  print (numero)
```

<h3>While</h3>

A sua estrutura pode ser dividida em 3 partes:
A palavra reservada while;
Uma condição que pode ser verdadeiraa ou falsa; e
Um bloco de código que você quer executar repetidamente

Exemplo:
```python
numero = 2

while numero < 5:
  print(numero)
  numero = numero+1
```

<h3>Quando utilizar o For e quando utilizar o While?</h3>

Finalidade: O for é geralmente usado quando se quer iterar sobre uma sequência (como uma lista, tupla, string ou qualquer objeto iterável) ou quando se sabe de antemão quantas vezes se quer executar um bloco de código.

Características:

Usa uma variável de iteração que percorre os valores de uma sequência.
Combina bem com a função range() para criar sequências numéricas.

Finalidade: O while é usado quando se quer executar um bloco de código enquanto uma condição específica for verdadeira. Portanto, não é necessário saber quantas vezes o bloco será executado de antemão.

Características:

Baseia-se em uma condição, e o bloco de código dentro do while é executado até que essa condição se torne falsa.
Pode levar a loops infinitos se a condição nunca se tornar falsa.
