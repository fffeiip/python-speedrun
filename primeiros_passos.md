# Primeiros Passos

## Instalação
Os passos seguintes foram criados de acordo com a [documentação](https://www.python.org/about/gettingstarted) encontrada no site oficial da linguagem.

### **Windows**
> - Entrar no [site oficial](https://www.python.org/downloads) e baixar o instalador oficial da linguagem. 
![python_installer](screenshots\primeiros_passos\download_python_installer.png)
> - Seguir passo a passo do instalador

**@TODO - Adicionar prints do passo a passo.**

### **MacOS**
> - Entrar no [site oficial](https://www.python.org/downloads/macos/) e baixar o instaldor oficial da linguagem.
> - Ou alternativamente, instalar usando o gerenciador de pacotes [homebrew](https://docs.brew.sh/Homebrew-and-Python). 

**@TODO - Adicionar prints do passo a passo.**

### **Linux**
Sistemas GNU/Linux mais recentes já possuem uma versão do python instalada junto com o sistema operacional. Podemos checar se o python foi instalado corretamente com o seguinte comando: 

```shell
$ wich python3
```
**inserir imagem do retorno aqui**

Para evitar conflitos com o Python do sistema operacional, sugere-se a instalação de um outro interpretador, que pode ser feita de 2 formas diferentes: através do de gerenciador de pacotes ou de repositórios.

**Gerenciador de Pacotes**

O gerenciador de pacote depende da distro linux utilizada. Os mais comuns são o apt-get (Debian, Ubuntu) e o yum (RedHat, CentOS). 
No momento que esta apostila foi escrita, a versão LTS do python era a versão 3.11.4

**Debian e Ubuntu**
```
$ sudo apt-get install python3.11
```
**RedHat e CentOS**
```
$ sudo yum install python3.11
```
**Por Repositório**

Os repositórios no GNU/Linux são chamados de PPAs (do inglês Personal Package Archives).

Para adicionar repositórios ao nosso sistema, precisamos de um software chamado software-properties-common, que pode ser instalado com o comando abaixo:
```
$ sudo apt-get install software-properties-common
```

Agora, é necessário adicionar o repositório que contém o Python, chamado de [deadsnakes](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa). 

```
$ sudo add-apt-repository ppa:deadsnakes/ppa
```
Atualizado o link de download do ppa, agora podemos fazer a instalação do python utilizando o seguinde comando: 

```
$ sudo apt-get install python3.11
```

> é possível instalar outras versões, basta substituir por: `python3.8`, `python3.9`, `python3.10`,

## Outras plataformas
É possível também instalar o python em outras plataformas através de binários e bibliotecas de terceiros, para tal, o site oficial disponibiliza as [instruções necessárias](https://www.python.org/download/other/). Contudo, tal conteúdo não é o foco da nossa apostila.
