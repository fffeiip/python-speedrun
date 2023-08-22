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

