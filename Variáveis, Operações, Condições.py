
"""
Regras de declaração
Case-sensitive (ou seja, caracteres em caixa alta ou baixa são tratados como diferentes)
DEVE começar com uma letra ou um sublinhado; NÃO PODE começar com números.
NÃO PODE ser o mesmo nome que as palavras-chave Python (por exemplo, class, finally, etc.)
NÃO especificar o tipo de informação armazenada na variável. (Consulte os seguintes códigos para um exemplo.)
"""

#______________________________________________Tipos____________________________________________

STRING = "Verdade!"
CHAR = 'f'
STRING += CHAR
INT = 10
FLOAT = 12.9
BOOL = True

#Repare que char e string são tratadas como mesmo tipo
print(type(STRING) ,"(STRING) = " ,type(CHAR) , "(CHAR)")

#______________________________________________Conversor de tipos____________________________________________

FLOAT += float(INT)#int -> float
INT += int(FLOAT)#float -> int
STRING += str(FLOAT)#float -> string

print("FLOAT = " ,FLOAT,"INT = " ,INT,"STRING = " ,STRING)

#______________________________________________Operações Matemática____________________________________________

print(10 + 2)#Soma
print(10 - 2)#Subtração
print(10 * 2)#Multiplicação
print(10 / 2)#Divisão
print(10 ** 2)#Potenciação
print(10 // 2)#Divisão com retorno inteiro
print(10 % 2)#Resto da divisão

#Operação com String e "Char"
print("_"*50)
print('a'*50)

#______________________________________________Concatenação____________________________________________

print("Teste" + str(50) + 'o' + "Caso")#Somente aceita tipos String

#______________________________________________Comparação____________________________________________

print(5 < 2)
print(5 > 2)
print(5 <= 2)
print(5 >= 2)
print(5 == 2)
print(5 != 2)

#______________________________________________Comparação de condição____________________________________________

x = 7
y = 14

#if else
if (2*x == y):
  print("y is double of x")
elif (x**2 == y):
  print("y is the squared of x")
else:
  print("y is NOT double of x")


#switch(não implementado no python)
def switcher(number):
  # Use dicionário (do Módulo 3) para armazenar switch cases
  # Se não for encontrado, o get() será o valor padrão
  return {
    '0':"Entered 0",
    '1':"Entered 1",
    '2':"Entered 2",
    '3':"Entered 3",
    '4':"Entered 4",
    '5':"Entered 5",
    '6':"Entered 6",
    '7':"Entered 7",
    '8':"Entered 8",
    '9':"Entered 9",
  }.get(number,"Invalid number!")

# input() lê uma entrado do usuário de stdin
number = input("Dial a number")
print()
switcher(number)


"""
EXERCÍCIO: implemente o exemplo de switch case acima usando as condições "if/else"

Prompt: para cada dígito entre 0-9, o programa imprimirá uma confirmação 
para o valor inserido ou irá imprimir "invalid inputs" para todos os outros números.
"""

number = input("Digite o número:")

if number == '0':
    print("Entered 0")
elif number == '1':
    print("Entered 1")
elif number == '2':
    print("Entered 2")
elif number == '3':
    print("Entered 3")
elif number == '4':
    print("Entered 4")
elif number == '5':
    print("Entered ")
elif number == '6':
    print("Entered 6")
elif number == '7':
    print("Entered 7")
elif number == '8':
    print("Entered 8")
elif number == '9':
    print("Entered 9")
else:
    print("Número Inválido!")