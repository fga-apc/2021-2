==========================
Plataformas de comunicação
==========================

MS Teams
========

O código de inscrição no MS Teams da UnB é 44v3y9y

Telegram
========

O link de inscrição para o grupo do Telegram é https://t.me/+r66rC_2ivg4wYjdh


Github
======

A página do curso no Github é https://github.com/fga-apc/2021-2


Checkio
=======

Crie uma conta no site http://checkio.org.



===============================
Ferramentas utilizadas no curso
===============================


VS Code
=======

Você pode utilizar o editor de código que preferir. Caso não possua nenhuma preferência, sugiro utilizar o Visual Studio Code, disponível gratuitamente em https://code.visualstudio.com/. Este é um dos editores de código mais versáteis e populares que existem e é relativamente leve, se configurado somente com os plugins necessários.

Todas as aulas serão gravadas utilizando o VSCode. Assim, utilizar o mesmo editor auxilia na curva de aprendizado e em descobrir truques novos durante as aulas ou perguntando para o professor.

Plugins
-------

O Visual Studio code precisa de alguns plugins para funcionar corretamente. Clique no botão de extensões (ou Ctrl + Shift + X) para ativar a barra de extensões. Procure pela extensão Python da Microsoft (o nome oficial é ms-python.python). Normalmente é a primeira mostrada na lista de resultados, antes mesmo de digitar Python na barra de busca.

A próxima extensão utilizada no curso é a de C/C++ da Microsoft (o nome oficial é ms-vscode.cpptools). Digite "C/C++" ou ms-"vscode.cpptools" na busca e a extensão correta corresponderá ao primeiro resultado. 


Python
======

É necessário utilzar o intepretador de Python. Sugiro baixar a última versão do instalador em https://www.python.org/. No momento, isto corresponde ao Python 3.10, mas qualquer versão igual ou maior que 3.8 funcionará perfeitamente. Versões antigas do Windows (Windows 7 ou anterior) funcionem não suportam Python 3.10 e devem utilizar o Python 3.8.

Testando o Python
-----------------

Crie uma pasta no seu computador para guardar os programas desenvolvidos ao longo do semestre e abra-a no Visual Studio Code utilizando o comando *Arquivo > Abrir Pasta*. Crie um novo arquivo chamado "teste.py" e copie e cole o código abaixo.

```python
print("OLÁ, PYTHON!")
print("TCHAU!")
```

Salve e execute o programa utilizando o botão de executar no canto superior direito ou o atalho `Ctrl + F5`. O VSCode deve mostrar algumas mensagens no terminal e as linhas "OLÁ, PYTHON!" e "TCHAU!", no final da execução. Se isto ocorrer, significa que a execução foi bem sucedida.  


Pyxel
=====

[Pyxel](https://github.com/kitao/pyxel) é uma biblioteca para a criação de jogos em Python. Num mundo ideal, o Pyxel pode ser instalado a partir do terminal do VS Code ou do Windows (Tecla Windows + R, depois digita "cmd"). O comando para isto seria "python -m pip install pyxel". Infelizmente, isto normalmente não funciona em algumas instalações, e é necessário utilizar outras alternativas mais complicadas.

Minha sugestão é abrir o VSCode e criar um programa novo com o seguinte conteúdo:

```python 
import pip
pip.main(["install", "pyxel"])
```

Execute o programa para instalar o Pyxel desta maneira. Use algum exemplo no site do Pyxel para testar se a instalação foi bem sucedida:

```python
import pyxel

pyxel.init(160, 120)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

pyxel.run(update, draw)
```


Compilador de C
===============

Utilizaremos o Tiny C Compiler (https://bellard.org/tcc/) e possivelmente outros.


Jupyter Notebook e IPython (opcional)
=====================================

Instale com o comando `pip install notebook ipython`


Outras tecnologias recomendadas
===============================

* Git
* Linux (Máquina Virtual)
* Linux (Dual Boot)