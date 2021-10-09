#a = 'acertou'
print('Hello world')
#resp = str(input("Deseja saber o tipo de a? "))
#if resp == 's':
#    print('o tipo de a é:', type(a))
#else:
#    print('Tudo bem então')
#x = int(input('digite o valor de x: '))
#y = int(input('digite o valor de y: '))
#print('A adição de : ', x ,'e', y ,'é: ', (x+y))
#print('A subtração de : ', x ,'e', y ,'é: ', (x-y))
#print('A multiplicação de : ', x ,'e', y ,'é: ', (x*y))
#print('A divisão de : ', x ,'e', y ,'é: ', (x/y))

#Elemtns of python
#O python lê linha por linha, e se você implementar
#uma condição de repetição ele irá reler

#Loops and iterations
#linha por linha até que satisfazer a condição proposta
#Estruturas em loop (Passos repetidos) tem variaveis de iteração
#que mudam (incrementa ou decrementa) cada vez que repete.

#A estrutura while é chamada de loop infinito porque
#o loop continua ativo ENQUANTO não atinge a condição proposta
def estruturawhile():
    print('Carregando pagamento diário...')
    n = 5
    while n > 0:
        print(n)
        n = n -1
    print('...Finalizado!')

#Definite loops
#Esses loops são chamados de loops finitos porque
#executam um exato numero de vezes
def estruturafor():
    for i in range(11):
        if i > 5:
            i + 1
            print('maior que 5')
            print(i)
        else:
            print('menor que 5')
            print('Acabou com i', i)
            print('finalizado')

#Variable, Expressions and Statements
#Procure priorizar a atribuição de variáveis
#com nomes intuitivos
def variaveis():
    hours = 35.0
    rate = 12.50
    pay = hours * rate
    print('O pagamento diário é:', pay)

#Intermediate Expressions
#As prioridades de cálculo de expressões são:
# 1 - Parentesis
# 2 - Potenciação
# 3 - Multiplicação e Divisão
# 4 - Soma e Subtração
# 5 - Da esquerda para a direita
def expressoesintermediarias():
    x = 1 + 2 ** 3 /4 * 5
    print('O resultado da expressão 1 + 2³/4 x 5 é =',x)

#Existem tipos de variáveis
#O que torna certas operações impossíveis
#Você não consegue somar texto+1 (string + inteiro)
#Mas você consegue concatenar String + String
def tipos():
    print(type(x))
    print(type('hello'))
    print(type(1))

#Podemos instruir o python a pausar e ler dados
#do usuário usando a função input()
#que por padrão, retorna uma string
def lerdados():
    nome = input('Quem é você? ')
    print ('Bem vindo:',nome)

#Se quisermos ler um numero do usuário devemos converter
#da String para um numero usando a função de conversão de tipos
def convertertipo():
    inp = input('Europe floor?')
    usf = int(inp) + 1
    print('US floor', usf)

#Conditional Execution
#caso seja uma condição de execução como um if
#ele irá pular a opção que não se encaixar na condição.
#O python liga muito sobre o quão a linha está identada
#se você misturar espaços e identação você terá "erros de identação"
#mesmo que tudo pareça normal
def execucaocondicional():
    x = int(input('Digite um valor maior que 4 e menor que 6:'))
    if x == 5:
        print('O valor é Igual a 5')
        if x > 4:
            print('O valor é maior que 4')
        if x >= 5:
            print('O valor é maior ou igual a 5')
        if x < 6:
            print('O valor é menor que 6')
        if x <= 5:
            print('O valor é menor ou igual a 5')
        if x != 6:
            print('O valor é diferente de 6')
        if x < 5:
            print('O valor precisa ser maior que 4')
        if x > 5:
            print('O valor precisa ser menor que 6')

#More Conditional Structures
#A estrutura condicional try except é usada para prever erros
#no código e prevenir que ele pare, o try funciona como "tente fazer isso"
#e o except funciona como "se não conseguir faça aquilo"
def tryexcept():
    varstringpadrao = 'oi igor'
    try:
        inteirostring = int(varstringpadrao)
    except:
        inteirostring = -1

    print ('primeiro', inteirostring)
#no código acima o que atribuimos a variavel varstringpadrao é uma string,
#ou seja uma cadeia de letras, entre o try e except estamos tentando
#atribuir o valor da varstringpadrao à outra variavel como um inteiro,
#o que não é possivel, pois o codigo nao consegue converter string em inteiro
#ou seja, não é possível converter caracteres em números,
#a estrutura condicional try isola este erro e faz com que o except execute
#a proxima opção implementada, que no caso é
#atribuir o valor -1 à variavel inteirostring
#se o try funciona a opção excpet é ignorada, se o try retorna um erro
#este erro é ignorado e o compilador executa o except
def tryexcept2():
    astr = '123'
    try:
        istr = int(astr)
    except:
        istr = -1

    print('segundo', istr)
#no codigo acima ocorre a mesma situação, mas o que foi atribuido à variável
#astr foram numeros, mesmo sendo declarando como string, foi possível
#converter a variável em inteiro e atribui-la à outra, no caso, a istr
#então o compilador conseguiu executar o try e ignorou o except
def tryexcept3():
    entrada = input('Entre com um número:')
    try:
        valorinteiro = int(entrada)
        print('o numero é', valorinteiro)
    except:
        valorinteiro = -1

        if valorinteiro > 0:
            print("Bom trabalho")
        else:
            print('Não é um numero')
            tryexcept3()

#Python functions
#No python funções são alguns codigos reutilizáveis que levam argumentos
#como entrada, fazem alguma computação e retornam reultados

#Build your own functions
#Argumento é um valor que passamos para a função como entrada (input)
#quando invocamos a função
#Ao usarmos argumentos podemos direcionar a função para diferentes tipos
#de trabalho quando incovamos em diferentes tempos
#nos colocamos argumentos entre parentesis apos o nome da função

#Um parametro é uma variavel que usamos na definição da função
#é um "guia" que permite o codigo na função a acessar os argumentos
#em uma invocação de função em particular

#O comando def gera e nomeia funções que podem ser invocadas à
#qualquer momento, à partir de "pedaços de código"
#de nossa preferencia.

def saudacao(linguagem):
    if linguagem == 'es':
        print('hola')
    elif linguagem == 'fr':
        print('bonjour')
    else:
        print('olá')

#O return termina a execução da função e "envia de volta" o resultado dela
#Quando a função nao retorna valor, chamamos isso de void
#Funções que retornam valores são "frutiferas"
#Funções void não são "Frutiferas"


#loop Idioms
#Numa tarefa para descobrir o maior numero, o computador não funciona comando
#O nosso cérebro, ele passar por cada valor, comparar com o maior anterior
#e assim atribui-lo à uma variavel.

def qualmaiornumero():

    omaior = None
    print('Antes', omaior)
    for i in [1, 2, 3, 45, 2, 4, 5, 46]:
        if omaior is None or i > omaior:
            omaior = i
        print(omaior, i)
    print('Depois', omaior)
#More Patterns
#Numa tarefa para calcular a média dos valores alocados em uma cadeia de numeros
#precisamos de uma variável que conte o numero de valores, uma variavel que some
#esses valores e o resultado será a soma dividido pelo numero de valores.
def calculodemedia():
    conta = 0
    soma = 0
    print('Antes', conta, soma)
    for valor in [10, 10, 10 ,10 , 10, 9]:
        conta = conta + 1
        soma = soma + valor
        print(conta, soma, valor)
    print ('Depois', conta, soma, soma/conta)

#existem outras formas de comparar, filtrar, saber se o valor está entre
#os valores de um array

#Strings in python
#Em python conseguimos percorrer uma string utilizando a estrutura for

#Intermediate Strings
#Nós também conseguimos retornar uma seção contínua da indexação do array
#de uma string utilizando o operador : (Dois pontos)
#o segundo parametro é além do fim da janela retornada
#por exemplo: str[1:3] só retornará as posições 0 1 2 da variavel str
#a lista retornada vai até o segundo parametro mas não o inclui
#se passamos parâmetros vazios para a fatia é assumido que será retornado
#do inicio ou o fim da string, por exemplo str[:3] retornará do incio até a
#2 lembrando que a posição 3 não será retornada.

#o in tambem pode ser usado como operador lógico de comparação
#se há n na variavel str atribua verdadeiro na variavel c
def existealetranapalavra():
    str = 'banana'
    if 'n' in str:
        c = True
    print(c)

#python tem um numero de funções para tratamento de string que estão
#na biblioteca string, essas funções já estao criadas em cada String
#nos as invocamos ao anexar a função à variavel String
def funcminusculo():
    str = 'BANANA'
    str2 = str.lower()
    print(str2)
    print(dir(str2))
#é possivel usar a função dir com um parametro string
#para saber mais sobre quais funções srting estão na biblioteca do python

#utilizamos a função find() para procurar por uma
#substring que possa estar em uma String
#ele retornará a primeira posição da indexação
#que seja igual a substring passada como parametro
def funcprocura():
    fruta = 'banana'
    existe = fruta.find('na')
    #"ache o primeiro na e me traga a posição"
    print(existe)
    aa = fruta.find('z')
    print(aa)
#"ache o primeiro na e me traga a posição"
#se a substring não for encontrada o find() retorna -1

#Função Search and Replace
#A função replace() substitui TODAS AS OCORRENCIAS da string de procura
#pela string de subistituição
def searchreplace():
    saudacao = 'Ola Igor'
    novastr = saudacao.replace('Igor', 'Luigi')
    print(novastr)

#Reading files
#A função open() é utilizada para carregar o arquivo
#o Nome do arquivo deve ser passado como parametro para a função
#e em seguida o modo em que o arquivo será carregado
#por exemplo, open('teste.txt', 'r') o modo utilizado é o de leitura
# 'r' para leitura e 'w' para escrita
def lerarquivo():
    x = open('teste', 'r')
    print(x)

#utilizamos o caractere especial \n chamado newline
#para indicar quando uma linda acaba


#Conseguimos usar um uma condição if em nosso loop for para apenas
#printar linhas que se encaixam em algum critério
def procuralinha():
    fhand = open('teste.txt')
    for line in fhand:
        if line.startswith('from:'):
            print(line)
# Procurando através de um arquivo
# A função rstrip() é utilizada para limpar os espaços
# em branco e do qual a "new line" é considerada
# line = line.rstrip()

# What does the word 'continue' do in the middle of a loop?
# Skips to the next iteration of the loop.

# Algoritmos: Uma cadeia de regras ou
# passos usados para resolver um problema
# Estrutura de dados: Uma forma particular
# de organizar os dados em um computador

# A função range() retorna uma lista de numeros
# que alcança do zero até um a menos do que o parametro
# friends = ['joseph', 'pollnaref', 'kayoin']
# print(range(len(friends)))
# retornará [0, 1, 2]

# Podemos construir um loop de indice usando o for e um inteiro iterador

def teste():
    friend = ['joseph', 'polnaref', 'kakyoin']
    for friend in friends:
        print('Wryyyyy:', friend)

def teste2():
    for i in range(len(friends)):
        friend = friends[i]
        print('Wryyyy:', friend)


#Working With Lists
#Podemos criar uma lista vazia e adicionar elementos usando o metodo append
#A ordem da lista é ditada pela ordem que adicionamos elementos no final dela
def declaralista():
    #declarando uma variável como lista vazia:
    coisa = list()
    #adicionando a string book ao final dessa lista:
    coisa.append('livro')
    coisa.append('Bolsa')
    coisa.append('Telefone')
    coisa.sort()
    print(coisa)
    print(coisa[0])
    if 99 in coisa:
        print('tem', 99,'em', coisa)

#declaralista()

#Funções para manipulação de listas
def funclistas():
    lista1 = [3, 4, 5, 6, 7, 8, 9, 1, 2]
    print('O tamanho da lista é', len(lista1))
    print('O maior valor da lista é', max(lista1))
    print('O menor valor da lista é', min(lista1))
    print('A soma de todas as posições da lista é', sum(lista1))
    print('O valor médio da lista é', sum(lista1)/len(lista1))

#Calcular a media de uma lista "infinita" com valores
#e tamanho ditadas pelo usuário
def medialista():
    total = 0
    count = 0
    while True:
        inp = input('enter a number')
        if inp == 'done': break
        value = float(inp)
        total = total + value
        count = count + 1
    average = total/count
    print('Average', average)

print('Bem-vindo aos casos de estudo do Igor')
opcoes = ['Para atribuição e cálculo de variáveis digite 1:',
 'Para expressões intermediátias digite 2:',
 'Para os tipos de variáveis digite 3:',
  'Para leitura de dados digite 4:',
   'Para conversão de tipo digite 5:',
   'Para estruturas condicionais digite 6:',
   'Para contenção de erros tryexcept digite 7:',
   'Para funções, argumentos e parametros digite 8:',
   'Para estutura de repetição para descobrir o maior numero, 9: ']
for i in opcoes:
    print(i)
entrada = input('Digite a opção: ')
entradaint = int(entrada)
if entradaint == 1:
    variaveis()
elif entradaint == 2:
    expressoesintermediarias()
elif entradaint == 3:
    tipos()
elif entradaint == 4:
    lerdados()
elif entradaint == 5:
    convertertipo()
elif entradaint == 6:
    entrada = input('Para estrutura for digite 1 e para while digite 2:')
    entradaint = int(entrada)
    if entradaint == 1:
        estruturafor()
    elif entradaint == 2:
        estruturawhile()
    else:
        print('Favor digitar opção válida')
elif entradaint == 7:
    def exercicio7():
        entrada = input('Exercicio 1, 2 ou 3?')
        try:
            entradaint = int(entrada)
            if entradaint == 1:
                tryexcept()
            elif entradaint == 2:
                tryexcept2()
            elif entradaint == 3:
                tryexcept3()
            else:
                print('Digite uma opção válida')
                exercicio7()
        except:
            entradaint = 0
            if entradaint < 1:
                print('Digite uma opção válida')
                exercicio7()
    exercicio7()
elif entradaint == 8:
    def escolhalinguagem():
        print('1 - Espanho')
        print('2 - Frances')
        print('3 - Portugues')
        entrada = input('Qual lingua?')

        entradaint = int(entrada)
        if entradaint == 1:
            saudacao('es')
        elif entradaint == 2:
            saudacao('fr')
        elif entradaint == 3:
            saudacao()
        else:
            print('digite um valor valido: ')
            escolhalinguagem()
    escolhalinguagem()
elif entradaint == 9:
    qualmaiornumero()

else:
    print('Favor digitar opção válida')
