## Gerenciador de pacotes Pip

### O que é um gerenciador de pacotes ?
O PIP é um gerenciador de pacotes Python que torna possível os usuários compartilharem e/ou utilizarem códigos de uma forma simples e prática.

### Verificando se o PIP está instalado
Digite na linha de comando:
```shell
$ pip --version
```
Caso ele esteja instalado, você deve ver algo como na imagem abaixo:

**@TODO - Adicionar print**

### Caso seja necessário instalar o PIP
- Baixe o [arquivo](https://bootstrap.pypa.io/get-pip.py) 
"get-pip.py" ou excute o comando abaixo:
```shell
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
- Com o prompt aberto no diretório onde foi baixado o arquivo, execute o comando abaixo:
```shell
$ python get-pip.py
```
Você deve ver algo como na imagem abaixo:

**@TODO - Adicionar print**

### Como instalar e desistalar um pacote com o PIP?
- Instalando um pacote
```shell
$ pip install <nomedopacote>
```
- Desisntalando um pacote
```shell
$ pip uninstall <nomedopacote>
```

### Listando todos os pacotes instalados com PIP
Caso você tenha instalado um pacote com PIP, será possível verificar se ele realmente já faz parte da sua lista de pacotes.

- Execute o comando abaixo:
```shell
$ pip list
```
Você deve ver algo como na imagem abaixo:

**@TODO - Adicionar print**
