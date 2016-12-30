# Algumas anotações do minicurso Google Python Day

Primeiro vídeo (veja os seguintes): https://www.youtube.com/watch?v=tKTZoB2Vjuk&feature=youtu.be

> Python era minha linguagem para qualquer trabalho na universidade. Após sair da academia, parei de usar. E voltei a estudar há algum tempo para melhorar como programador e explorar áreas afins

A grande fonte de atraso no seu trabalho de programa é bug. Se um erro ficar escondidinho (como não gerar usar uma variável nunca atribuída), pode ser um problema. Python não deixa isso passar.

    >>> 
    >>> 'Hello' + 6
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: cannot concatenate 'str' and 'int' objects
    >>> 
    >>> 'Hello' + str(6)
    'Hello6'
    
## Acentuação e caracteres especiais em programas Python

Erro encontrado:

	File "foo.py", line 2
	SyntaxError: Non-ASCII character '\xc3' in file foo.py on line 2, but no
	encoding declared;see http://www.python.org/peps/pep-0263.html for details

Por padrão, Python 2.7 interpreta Non-ASCII. Indique explicitamente no começo do código encoding que você deseja usar:

	#!/usr/bin/python
	# coding=<encoding name>

or (using formats recognized by popular editors)

	#!/usr/bin/python
	# -*- coding: <encoding name> -*-

Exemplo:

	#!/usr/bin/python
	# coding=UTF-8

Fonte:
https://pythonhelp.wordpress.com/2011/09/03/acentuacao-em-programas-python/
https://www.python.org/dev/peps/pep-0263/


## Comandos úteis do prompt Python

	>>> import sys

`dir(sys)` → mostra propriedade e métodos de sys
`help(sys)` → mostra um manual do sys
`help(sys.exit)` → mostra um manual de uma função de sys

Ao usar `sys.exit()`, você está executando o método. Ao usar: `sys.exit`, você só está está fazendo referência

## Dicas diversas

Se você usa um símbolo, você precisa ter o definido anteiormente

`==` em python comparar muito bem qualquer coisa. Não precisa usar `===` (dará erro).

No `if`, não precisa usar parênteses. E é uma boa prática do python que você não utilize

Python não olha o código todo para saber se está tudo ok e bem definido. Ele sempre olha no último momento. Se você tem uma função não definida em um trecho de código que não é alcançado, não haverá erro
	Por causa disso, sugere-se muito ter cobertura de teste ;)
	Então você executará tudo para saber se tem erro

# Algumas coisas sobre `String`

`Strings` são imutáveis. Sempre cria um novo valor

	>>> b = 'YAY'
	>>> b.lower()
	'yay'
	>>> b
	'YAY'
	>>> 

Uso de `%` para strings (como em C etc.)

	>>> 'Hi %s I have %d donuts' % ('Alice', 43)
	'Hi Alice I have 43 donuts'
    
    
    >>> a = 'Hello'

Tratando `Strings` como listas. Tirando substrings

    >>> 
    >>> a[0]
    'H'
    >>> a[1]
    'e'
    >>> len(a)
    5
    >>> a[1:3] → começa do 1 e vai até 3, MAS NÃO INCLUSO
    'el'
    >>> 
    >>> a[1:]
    'ello'
    >>> a[-1]
    'o'
    >>> a[-3:-1]
    'll'
    >>> a[-3]
    'l'
    >>> a[-3:]
    'llo'


# A diretiva `t-`

Pode ser usada ao executar uma script python

O que faz a `-t`?
> Issue a warning when a source file mixes tabs and spaces for indentation in a way that makes it depend on the worth of a tab expressed in spaces. Issue an error when the option is given twice (-tt).

Exemplo de erro:

    $ python -t hello.py Joston
    hello.py: inconsistent use of tabs and spaces in indentation
    Alert: Joston Mode
    Hello Joston????!!!!
    $ python -tt hello.py Joston
      File "hello.py", line 10
        name = name + '????'
                           ^
    TabError: inconsistent use of tabs and spaces in indentation
    
# Python é consistente 

> Python tenta ser consistente nas funções. len() funciona pra string e lista. + tbm etc.

# Listas

Lists são mutáveis

    >>> a = [1,2,3]
    >>> b = a
    >>> b
    [1, 2, 3]
    >>> a[0]
    1
    >>> a[0] = 13
    >>> a
    [13, 2, 3]
    >>> b
    [13, 2, 3]
    >>> b = a[:] ← how to make copy
    >>> b[0] = 23
    >>> a
    [13, 2, 3]
    >>> b
    [23, 2, 3]
    >>> 


	>>> for num in a: print num
	... 
	13
	2
	3


    >>> b
    [31, 2, 3]
    >>> 2 in b
    True
    >>> 22 in b
    False
    >>> 

 
    >>> b
    [31, 2, 3]
    >>> b.append(6) ← append NÃO retorna uma lista. modifica a lista somente!
    >>> b
    [31, 2, 3, 6]
    >>> 


    >>> b
    [31, 2, 3, 6]
    >>> b.pop(0) ← remove o elemento da posição 0 e retorna pra mim
    31
    >>> b
    [2, 3, 6]
    >>> 

    >>> a
    9
    >>> del a
    >>> a
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'a' is not defined
    >>> a = [1,2,3]
    >>> a
    [1, 2, 3]
    >>> a[1]
    2
    >>> del a[1]
    >>> a
    [1, 3]


## Ordenando

    >>> a = [4,2,1,6]
    >>> sorted(a) ← cria uma nova lista e retorna
    [1, 2, 4, 6]
    >>> a
    [4, 2, 1, 6]

    >>> a = ['ccc', 'aaaa', 'd', 'bb']
    >>> sorted(a)
    ['aaaa', 'bb', 'ccc', 'd'] ← quero ordernar pelo tamanho!


    >>> a = ['ccc', 'aaaa', 'd', 'bb']
    >>> sorted(a)
    ['aaaa', 'bb', 'ccc', 'd']
    >>> len
    <built-in function len>
    >>> sorted(a, key=len)
    ['d', 'bb', 'ccc', 'aaaa']


## Ordenando por um parâmetro específico

    >>> a[1] = 'aaaz'
    >>> def Last(s): return s[-1]
    ... 
    >>> Last
    <function Last at 0x7f78ae578578>
    >>> sorted(a, key=Last)
    ['bb', 'ccc', 'd', 'aaaz']


## O velho join
    >>> a
    ['ccc', 'aaaz', 'd', 'bb']
    >>> 
    >>> ':'.join(a)
    'ccc:aaaz:d:bb'
    >>> ', '.join(a)
    'ccc, aaaz, d, bb'
    >>> '\n '.join(a)
    'ccc\n aaaz\n d\n bb'


## Split

    >>> b = ':'.join(a)
    >>> b
    'ccc:aaaz:d:bb'
    >>> b.split(':')
    ['ccc', 'aaaz', 'd', 'bb']


## Populando uma lista

    >>> result = []
    >>> for s in a: result.append(s)
    ... 
    >>> result
    ['ccc', 'aaaz', 'd', 'bb']


## Iterando

    >>> range(20)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    >>> for i in range(20): print i
    ... 
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19


# Tuplas

Uma forma anônima de pegar um número fixos de coisas e travá-los juntos. São imutáveis

    >>> (1,2,3)
    (1, 2, 3)
    >>> a = (1,2,3)
    >>> a
    (1, 2, 3)
    >>> len(a)
    3
    >>> a[2]]
      File "<stdin>", line 1
        a[2]]
            ^
    SyntaxError: invalid syntax
    >>> a[2]
    3
    >>> a[2] = 3
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

Dado o critério de ordenação: ordene pelo primeiro elemento. se forem iguais, pelo segundo. E assim por diante. Uma idéia, usa uma lista no método sorted() onde a key function é retorna tuplas. Lista de tuplas são ordenadas assim! Exemplo:

    >>> a = [(1, "b"), (2, "a"), (1, "a")]
    >>> a
    [(1, 'b'), (2, 'a'), (1, 'a')]
    >>> sorted(a)
    [(1, 'a'), (1, 'b'), (2, 'a')]

Usando a sintaxe de tuplas para atribuir múltimas variáveis também

    >>> (x, y) = (1, 2)
    >>> (x, y)
    (1, 2)
    >>> x
    1
    >>> y
    2
    >>> 

> Slicing works with touples

# Dicionário

    >>> d = {}
    >>> d['a'] = 'alpha'
    >>> d['o'] = 'omega'
    >>> d['g'] = 'gamma'
    >>> d
    {'a': 'alpha', 'g': 'gamma', 'o': 'omega'}
    >>> d['a']
    'alpha'

> Um dicionário é muuito rápido. Custo é constante. Mesmo com milhões de registros, o dado é recuperado com em poucos ciclos de clock

    >>> d.keys()
    ['a', 'g', 'o'] ← note que está em ordem aleatória!! faz parte da estratégia de performance do dicionário
    >>> d.values()
    ['alpha', 'gamma', 'omega']
    >>> 

Note que o dicionário fica em ordem aleatória

    >>> d['x']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'x'
    >>> d.get('x') ← assim retorna None, caso não existe (em vez de erro)
    >>> d.get('a')
    'alpha'


## Como verificar se o dado existe no dicionário?

    >>> 'a' in d
    True
    >>> 'x' in d
    False

## Como fazer loop no dicionário?

    >>> for k in sorted(d.keys()): print 'key:', k, '->', d[k]
    ... 
    key: a -> alpha
    key: g -> gamma
    key: o -> omega
    >>> 

    >>> d.items()
    [('a', 'alpha'), ('g', 'gamma'), ('o', 'omega')]
    >>> 
    >>> for tuple in d.items(): print tuple
    ... 
    ('a', 'alpha')
    ('g', 'gamma')
    ('o', 'omega')


Dicionário é muito útil para organizar dados desorganizados muito grandes, como log. Associar dados aleatórios. Qualquer chave aleatória pode ser acessada muito, muito rapidamente

# Arquivos

    def Cat(filename):
            f = open(filename, 'rU')
            for line in f:
                    # print line # por padrão, isso coloca  uma linha extra no final
                    print line,
      f.close() # se vc omite, ele fecha quando o processo termina

Esta abordagem (acima) de ler o arquivo linha a linha é otimizada e não carrega o arquivo todo na memória. Mas se você a abordagem a seguir, usará a ram do tamanho do arquivo:

    def Cat(filename):
      f = open(filename, 'rU')
      lines = f.readlines()
      print lines
      f.close() # se vc omite, ele fecha quando o processo termina
      
E read() traz uma string

    def Cat(filename):
      f = open(filename, 'rU')
      text = f.read()
      print text,
      f.close() # se vc omite, ele fecha quando o processo termina
      
Criar um arquivo
    f = open(filename, 'w')
    f.write(text)
    
Em linguagens como Java ou C, há declaração de tudo e você sabe o que é aquilo. Em Python, como tudo é dinâmico, tudo que acontece no código está na sua cabeça. Logo, colocar nomes bons de variáveis é 10x mais importante do que em qualquer outra linguagem

Sugere-se também aproveitar as propriedades do python para fazer o programa incrementalmente. Testando incremento e incremento (e não fazer um código todo para testar no final)

# Expressão regular <3

    >>> import re
    >>> match = re.search('iig', 'called piiig') ← returns a match object
    >>> match
    <_sre.SRE_Match object at 0x7fccbd621370>
    >>> match.group()
    'iig'
    >>> 


    >>> match = re.search('igs', 'called piiig') ← match points to nothing
    >>> match
    >>> match.group()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'NoneType' object has no attribute 'group'
    >>> 

Então é importante testar if match:

    >>> def Find(pat, text):
    ...   match = re.search(pat, text)
    ...   if match: print match.group()
    ...   else: print 'not found'
    ... 
    >>> Find('ig', 'called piiig')
    ig
    >>> 

## Pequena referência:

`.`	(dot) any char
`\w`	word char
`\d`	digit
`\s`	whitespace ← espaço, tab etc. Mas 2 espaços não funciona
`\S`	NON whitespace
`+`	1 or more
`*`	0 or more

## Alguns exemplos:

any three chars and then a g
    >>> Find('...g', 'called piiig')
    iiig
    >>> 
1º solução da est → dir e para
    >>> Find('..g', 'called piiig much better: xyzg')
    iig
    >>> 

Não precisa usar `\`
    >>> Find('c\.l', 'c.lled piiig much better: xyzg')
    c.l
    >>> Find(r'c.l', 'c.lled piiig much better: xyzg') 
    c.l


    >>> Find(r'\d\s\d\s\d', '1 2 3')
    1 2 3
    >>> Find(r'\d\s+\d\s+\d', '1   2             3')
    1   2             3
    >>> 


space não conta como `\w` char
    >>> Find(r':\w+', 'blah blah :kitten blah blah')
    :kitten

    >>> Find(r':\w+', 'blah blah :kitten234& blah blah')
    :kitten234

`.` é tudo, menos nova linha
    >>> Find(r':.+', 'blah blah :kitten234& blah blah')
    :kitten234& blah blah


    >>> Find(r':\S+', 'blah blah :kitten23&$a=13&kj blah blah')
    :kitten23&$a=13&kj

Não dá certo porque o `.` não está em `\w`:
    >>> Find(r'\w+@\w+', 'blah blah nick.p@gmail.com yatta @ d')
    p@gmail


Usamos o `[]` para um conjunto de possíveis valores. Aqui é `\w` ou `.`
O `.` dentro do `[]` é considerado um ponto mesmo
	>>> Find(r'[\w.]+@\w+', 'blah blah nick.p@gmail.com yatta @ d')
	nick.p@gmail
	>>> 

    >>> Find(r'[\w.]+@[\w.]+', 'blah blah nick.p@gmail.com yatta @ d')
    nick.p@gmail.com

    >>> Find(r'[\w.]+@[\w.]+', 'blah blah .nick.p@gmail.com yatta @ d')
    .nick.p@gmail.com
    
O primeiro tem que ser um char e depois, seguidos de 0 ou mais `\w` até o @
    
    >>> Find(r'\w[\w.]*@[\w.]+', 'blah blah .nick.p@gmail.com yatta @ d')
    nick.p@gmail.com
    >>> 

Usa parênteses para dizer os trechos que você quer extrair
Se tirarmos o + e colocarmos no lado direito do parênteses, ele não extrai múltiplas vezes, mas muda o q é extraído

    >>> m = re.search(r'([\w.]+)@([\w.]+)', 'blah blah nick.p@gmail.com yatta @ d')>>> m.group()
    'nick.p@gmail.com'
    >>> m.group(1)
    'nick.p'
    >>> m.group(2)
    'gmail.com'
    >>> 

    >>> re.findall(r'[\w.]+@[\w.]+', 'blah blah nick.p@gmail.com yatta foo@bar d')['nick.p@gmail.com', 'foo@bar']

    >>> re.findall(r'([\w.]+)@([\w.]+)', 'blah blah nick.p@gmail.com yatta foo@bar d')
    [('nick.p', 'gmail.com'), ('foo', 'bar')]

Se há parênteses, python retorna túplas
    >>> re.findall(r'([\w.]+)(@)([\w.]+)', 'blah blah nick.p@gmail.com yatta foo@bar d')
    [('nick.p', '@', 'gmail.com'), ('foo', '@', 'bar')]
    >>> 


    >>> dir(re)
    ['DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', '_alphanum', '_cache', '_cache_repl', '_compile', '_compile_repl', '_expand', '_pattern_type', '_pickle', '_subx', 'compile', 'copy_reg', 'error', 'escape', 'findall', 'finditer', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'sys', 'template']
    
Em que:
`'IGNORECASE'` → lower or upper case the same
'DOTALL'` → Originalmente, . é any char, except for new lines (historical thing). Com `DOTALL`, também com nova linha

	>>> re.findall(r'([\w.]+)@([\w.]+)', 'blah blah nick.p@gmail.com yatta foo@bar d', re.IGNORECASE)
	[('nick.p', 'gmail.com'), ('foo', 'bar')]
    
    
# OS and commands

    >>> dir(os)
    >>> help(os.listdir)

copia arquivos
    >>> import shutil
    >>> shutil.copy(source, dest)


    >>> import commands
    >>> help(commands.getstatusoutput)

# URL Lib

abre, tenta tratar como arquivo. retorna stream (parece temporário! se executar o read duas vezes, na segunda está vazia)
    >>> import urllib
    >>> uf = urllib.urlopen('http://google.com') 
    >>> uf.read()
    '<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="pt"><head><meta content="text/html; …'

`urlretrieve` faz o download do asset

    >>> urllib.urlretrieve('http://google.com/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png', 'blah.git')
    ('blah.git', <httplib.HTTPMessage instance at 0x7f65d5755560>)
    >>> 

# Pensamentos finais

Sintaxe curiosa para criar listas a partir de outras (python list comprehension)
Usar esse tipo de sintaxe para coisas pequenas. Evitar usar para compactar e aninhar uma grande quantidade de código. Apesar do poder, prejudica bastante a legibilidade, o que é extremamente relevante.

    >>> a = ['aaaa', 'bb', 'cccc']
    >>> a
    ['aaaa', 'bb', 'cccc']
    >>> result = []

aplica a função à esquerda para cada `s` em `a`:
    >>> [ len(s)   for s in a      ] 
    [4, 2, 4]
    >>> 

    >>> a = [1, 2, 3, 4]
    >>> a
    [1, 2, 3, 4]

aplica a função à esquerda para cada s em a:
    >>> [ num*num  for num in a] 
    [1, 4, 9, 16]

usa a condicional à direita:
    >>> [ num*num  for num in a   if num > 2  ]
    [9, 16]

    >>> import os
    >>> import re
    >>> os.listdir('.')
    ['copyspecial.py', 'bli.zip', 'zz__something__.jpg', 'xyz__hello__.txt', 'solution', 'foo']
    >>> [ f   for f in os.listdir('.')   if re.search(r'__\w+__', f)  ]
    ['zz__something__.jpg', 'xyz__hello__.txt']
    >>> 

## Mais alguns dizeres

* O jeito que você aprende as coisas é programando.
* Melhorei minhas habilidades com python quando forcei a resolver problemas usanto python
* Python é bom para substituir códigos complexos de bash para tratar lista de arquivos, organizar etc