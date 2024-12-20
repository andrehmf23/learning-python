
#______________________________________________Lista____________________________________________

# Iniciar uma lista vazia
list1 = []
# OU
#list1 = list()

# Iniciar uma lista com elementos
list2 = ['hello', 'hola', 'olá']

#Uma lista pode comportar diversos tipos de dados
list3 = ["John", "male", 20, False]

print("First element in list2 : "+ list2[0])
print("Second element in list2 : "+ list2[1])

#Insere dado na posição específica
list2.insert(1,'hallo')
print(list2[1])


#Insere dado no fim da fila
list2.append('bye')
print(list2)

#Tenta remover da lista o dado passado
list2.remove('hello')
print(list2)

list2.append("hello")
print(list2)

#Remove ultima dao da fila
list2.pop()
print(list2)

#Ordena dados da lista
list2.sort()
print(list2)


# Imprimir itens na lista como string, separados por uma vírgula
",".join(list2)


# Você também pode ter uma lista de listas. Por exemplo:
lists = []
lists.append([1,2,3])
lists.append(['a','b','c'])

print(lists[1][0])

#______________________________________________Tupla____________________________________________
#Tupla é uma lista imutavel

# Inicializar uma tupla vazia
y = tuple()

# Criar uma nova tupla de elementos
x = (1,2,3)
print(type(x))

# ERROR: não pode ser adicionado a uma tupla
#x.append(4)

a,b,c = 1,2,3

# Declarar uma nova tupla, nome "person"
person  = ('Jane','Doe', 21)

# "Pacote"/associar cada elemento da tupla com uma etiqueta. Observe a ordem das etiquetas.
first, last, age = person

x = [1,2,3,4]
a,b,c,d = x


#_____________________________________________Conjunto_____________________________________________
#Conjunto: uma estrutura de dados mutável que armazena objetos não duplicados e imutáveis e ordena
# os elementos em ordem ascendente. Cada elemento do conjunto é único.

# Um conjunto com elementos
ex1 = {1, 2, 2, 1, 1}
print(ex1)

ex2 = {j for j in range(10)}
print(ex2)

ex2.add(2)
ex2.add(100)
ex2.add(50)
print(ex2)


#_____________________________________________Conversor_____________________________________________

# Converter uma lista em um conjunto
ages = [10, 5, 4, 5, 2, 1, 5]

set_of_ages = set(ages)

print(set_of_ages)

# Converter um conjunto em uma lista
list_of_ages = list(set_of_ages)

print(list_of_ages)

# Converter um conjunto em uma tupla
tuple_of_ages = tuple(list_of_ages)

print(tuple_of_ages)

#{1,2,3} == {2,1,3} -> True




#_____________________________________________Dicionário_____________________________________________

dict = {}

# Declare um dicionário com pares de chaves/valores
dict2 = {'a': 5, 'b': 10, 'c': 100, 'd': 9.5}

print(dict2['b'])

dict["greeting"] = "hello message"
dict["alphabet"] = ['a', 'b', 'c', 'd', 'e']
dict["check-in"] = False
dict["phoneNumber"] = 8007782346

# Podemos também buscar todas as chaves
dict.keys()
# Ou todos os valores
dict.values()
# Os elementos de um dicionário também podem retornar como um par.
dict.items()
